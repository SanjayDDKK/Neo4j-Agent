import streamlit as st
import uuid

def write_message(role: str, content: str, save: bool = True):
    if save:
        st.session_state.messages.append({"role": role, "content": content})
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

def get_session_id() -> str:
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id
