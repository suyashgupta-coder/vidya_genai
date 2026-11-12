
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

# Page configuration
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 AI Personality Chatbot")
st.write("Choose your personality and start chatting!")

# Personalities
personalities = {
    "Funny 😂": "You are a funny and witty AI agent. Answer every topic with relevant jokes and humor.",

    "Angry 😡": "You are an angry AI agent. Answer every topic with an angry tone while staying relevant.",

    "Sarcastic 😏": "You are a sarcastic AI agent. Answer every topic with sarcasm while staying relevant.",

    "Sad 😢": "You are a sad AI agent. Answer every topic with a sad and emotional tone while staying relevant.",

    "Romantic ❤️": "You are a romantic AI agent. Answer every topic with a romantic tone while staying relevant."
}

# Sidebar
st.sidebar.title("Settings")

choice = st.sidebar.selectbox(
    "Choose your personality",
    list(personalities.keys())
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        role = "user"
    else:
        role = "assistant"

    with st.chat_message(role):
        st.write(message.content)

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Create LangChain messages
    messages = [
        SystemMessage(content=personalities[choice])
    ] + st.session_state.messages

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = model.invoke(messages)

            answer = response.content

            if isinstance(answer, list):
                answer = "".join(
                    item.get("text", "")
                    if isinstance(item, dict)
                    else str(item)
                    for item in answer
                )

            st.write(answer)

    # Save AI response
    st.session_state.messages.append(
        AIMessage(content=answer)
    )