import streamlit as st
from agent import generate_response

st.title("Movie Agent")
query = st.text_input("What do you want to know about movies?")
if query:
    response = generate_response(query)
    st.write(response)