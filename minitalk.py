import streamlit as st
 import OpenAI

# ⛔ Yahan apni OpenAI API key paste karo (example: sk-abc123xyz...)
client = OpenAI(api_key="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")

# Page config & title
st.set_page_config(page_title="Mimi Chat App 💖", layout="centered")
st.title("💖 Mimi Chat App")
st.write("Hi! Main hoon **Mimi**, tumhari pyari chatbot! 😄 Mujhse kuch bhi poochho!")

# Chat history setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Tum kya kehna chahte ho? 👇")

if user_input:
    st.session_state.chat_history.append(("👧 Tum", user_input))

    # OpenAI ke latest SDK se response lo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tum ek pyari, masti bhari chatbot ho jiska naam Mimi hai. Tum funny, sweet aur doston jaisi feel deti ho."},
            {"role": "user", "content": user_input}
        ],
    )

    # Reply ko dikhana
    bot_reply = response.choices[0].message.content
    st.session_state.chat_history.append(("🤖 Mimi", bot_reply))

# Chat history display
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
import streamlit as st
from openai import OpenAI

# ⛔ Yahan apni OpenAI API key paste karo (example: sk-abc123xyz...)
client = OpenAI(api_key="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")

# Page config & title
st.set_page_config(page_title="Mimi Chat App 💖", layout="centered")
st.title("💖 Mimi Chat App")
st.write("Hi! Main hoon **Mimi**, tumhari pyari chatbot! 😄 Mujhse kuch bhi poochho!")

# Chat history setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Tum kya kehna chahte ho? 👇")

if user_input:
    st.session_state.chat_history.append(("👧 Tum", user_input))

    # OpenAI ke latest SDK se response lo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tum ek pyari, masti bhari chatbot ho jiska naam Mimi hai. Tum funny, sweet aur doston jaisi feel deti ho."},
            {"role": "user", "content": user_input}
        ],
    )

    # Reply ko dikhana
    bot_reply = response.choices[0].message.content
    st.session_state.chat_history.append(("🤖 Mimi", bot_reply))

# Chat history display
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
