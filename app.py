import streamlit as st
import json
import re
from langchain_groq import ChatGroq


# Load responses from JSON
@st.cache_data
def load_responses():
    with open('responses.json', 'r') as file:
        return json.load(file)

responses = load_responses()

# Match user input with patterns
def get_response(user_input,context=""):
    llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192", groq_api_key="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")
   
    prompt = f"""
    Given the user's question below, find the best matching user input from the context and return the associated answer.

    Context:
    {context}

    previous chat :
    {st.session_state.history}

    Question:
    {user_input}

    Instructions:
    1. Only respond using answers exactly as provided in the context.
    2. If the question does not match any entry in the context, reply with: "Sorry, I don't know."
    3. Do not generate new or inferred answers.
    4. Match the question as literally and precisely as possible.
    5. Only give the answer without any additional text.
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
