from flask import Flask, render_template, jsonify, request, session
from flask_session import Session
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.chat_models import ChatOllama 
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Load environment variables
load_dotenv()
os.environ['PINECONE_API_KEY'] = os.environ.get('PINECONE_API_KEY')

# Load embeddings and vector store
embeddings = download_hugging_face_embeddings()
index_name = "medicalbot"
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={'k': 5})

# Initialize model and prompt


llm = ChatOllama(
    model="llama3",
    temperature=0.4,
    max_tokens=500
)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.before_request
def setup_session():
    if 'chat_history' not in session:
        session['chat_history'] = []

@app.route("/")
def index():
    session['chat_history'] = []  # Clear chat on new visit
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]

    # Reconstruct previous chat history for context
    chat_history = session.get('chat_history', [])
    combined_input = "\n".join(
        [f"User: {c['user']}\nBot: {c['bot']}" for c in chat_history]
    )
    full_input = combined_input + f"\nUser: {msg}" if combined_input else msg

    # Get response from RAG chain
    response = rag_chain.invoke({"input": full_input})
    answer = response["answer"]

    # Store current turn in session
    chat_history.append({"user": msg, "bot": answer})
    session['chat_history'] = chat_history

    return jsonify({"response": answer})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(session.get('chat_history', []))

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
