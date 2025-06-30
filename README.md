# 🧠 GenAI Medical Chatbot

A Retrieval-Augmented Generation (RAG)-based **Medical Assistant Chatbot** built using **Flask**, **LangChain**, **Pinecone**, **HuggingFace Embeddings**, and **LLaMA3** (via Ollama or local inference). This chatbot helps users get intelligent answers from indexed medical documents.

🔗 GitHub Repo: [GenAI-Medical-Chatbot](https://github.com/Akash007AD/GenAI-Medical-Chatbot)

---

## ✨ Features

- ⚡ **RAG-based Architecture** using LangChain
- 🧾 **Medical Document Q&A** via Pinecone Vector Store
- 🧠 **LLM-powered responses** (supports local LLaMA3)
- 📊 Embeddings using HuggingFace
- 💬 Session-based chat history with Flask
- 🧩 Modular code (helper, prompt, routes)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Akash007AD/GenAI-Medical-Chatbot.git
cd GenAI-Medical-Chatbot
````

---

### 2. Create and Activate a Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate   # On Windows
# source myenv/bin/activate  # On Linux/macOS
```

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following:

```
PINECONE_API_KEY=your_pinecone_api_key
```

Make sure your Pinecone index is already created with the name `medicalbot`.

---

### 5. Run the App

```bash
python app.py
```

Then open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

---

## 💬 How It Works

* Documents are embedded using `sentence-transformers/all-MiniLM-L6-v2`.
* The embeddings are stored and queried from a Pinecone index.
* Queries are passed to an LLM (`llama3`) for response generation with contextual retrieval.
* The chat interface uses Flask templates and handles session history per user.

---

## 🤝 Acknowledgements

* [LangChain](https://www.langchain.com/)
* [Pinecone](https://www.pinecone.io/)
* [HuggingFace](https://huggingface.co/)
* [Ollama](https://ollama.com/) for local LLaMA inference

---

## 📜 License

This project is licensed under the **MIT License**.
