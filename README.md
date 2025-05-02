# 🤖 Rule-Based Chatbot using Langchain + Groq

A lightweight chatbot built with **Streamlit** and powered by **LLaMA3** via **Groq**. This chatbot only responds using predefined answers from a `responses.json` file. If the user asks something outside the provided context, it politely declines.

---

## 🚀 Features

- ✅ Simple, interactive chat interface via Streamlit  
- ✅ Response logic powered by `responses.json`  
- ✅ Integration with LangChain and Groq’s `llama3-70b` model  
- ✅ Strictly rule-based: no hallucinations  
- 🚫 Responds with _"sorry, I don't know"_ if the question is out of scope  

---

## 🧠 Example `responses.json`

```json
{
  "How are you?": "I'm just a bunch of code, but I'm doing great!",
  "What is AI?": "AI stands for Artificial Intelligence, which enables machines to simulate human intelligence."
}
```
# 📦 Installation
- git clone https://github.com/your-username/rule-based-chatbot.git
- cd rule-based-chatbot
- pip install -r requirements.txt
- groq_api_key = "your_groq_api_key"

# ▶️ Running the App
- streamlit run app.py

# 🛠 How It Works
- Loads question-answer pairs from responses.json.
- Accepts user input and sends it to Groq’s LLaMA3 model.
- The prompt constrains the model to:
- Only use answers present in the context
- Say "sorry, I don't know" for unknown inputs

# ❗Notes
- This is not a generative chatbot. It mimics one but only replies with known answers.
- Add more patterns/responses to responses.json for better coverage.
