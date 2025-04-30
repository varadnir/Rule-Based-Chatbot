import streamlit as st
import json
import re
from langchain_groq import ChatGroq


# Load responses from JSON
@st.cache_data
def load_responses():
    with open('responses.json', 'r') as file:
        print("Extracted")
        return json.load(file)

responses = load_responses()

# Match user input with patterns
def get_response(user_input,context=""):
    llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192", groq_api_key="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")
   
    prompt = f"""You are given a jason containing user response and answer, give the appropriate response using the given context and answer:

    Context:
    {context}

    Question:
    {user_input}

    note: 
    1. only use the answers present in the context.
    2. If the question is not present in the context, answer with "sorry, I don't know".
    Answer:"""

    response = llm.invoke(prompt)
    return response.content
        
    

# Streamlit UI
st.title("🤖 RuleBot - Chatbot")
st.markdown("Ask me anything! (Try questions like *hello*)")

# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.text_input("You:", key="input")

if user_input:
    bot_response = get_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_response))

# Display chat history
for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
