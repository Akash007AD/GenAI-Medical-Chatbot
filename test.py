import requests
import os

api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
  "model": "llama3-8b-8192",
  "messages": [{"role": "user", "content": "Who are you?"}]
}

response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
print(response.status_code)
print(response.json())
