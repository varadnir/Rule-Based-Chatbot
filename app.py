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
   
    prompt = f"""You are given a json containing user input and their response, give the appropriate response using the given context and answer:

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
        
    
# ✅ Page Configuration

# ✅ App Title and Description
st.title("🤖 Rule-Based Chatbot")
st.markdown("Welcome! Ask me anything and I'll reply based on predefined rules.")

st.divider()

# ✅ Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ User Input Section
user_input = st.chat_input("💬 Type your message here...")

if user_input:
    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get rule-based response (replace with your logic)
    ai_response = get_response(user_input,responses)

    # Append and display bot response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    
