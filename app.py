import streamlit as st
from langchain.messages import HumanMessage

from agent import agent

st.set_page_config(page_title="GPA/CGPA Agent", page_icon="🎓", layout="centered")

st.title("🎓 GPA / CGPA Agent")
st.caption(
    "Ask about your GPA, CGPA projections, or what you need to hit a target — PUCIT BS(CS)"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past conversation
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.text)
    elif msg.__class__.__name__ == "AIMessage" and msg.text:
        with st.chat_message("assistant"):
            st.markdown(msg.text)

# New input
user_input = st.chat_input("Ask something, e.g. 'What's my GPA if I got 78, 85, 64?'")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(HumanMessage(user_input))

    with st.chat_message("assistant"):  # noqa: SIM117
        with st.spinner("Thinking..."):
            result = agent.invoke({"messages": st.session_state.messages})
            reply = result["messages"][-1].text
            st.markdown(reply)

    st.session_state.messages = result["messages"]
