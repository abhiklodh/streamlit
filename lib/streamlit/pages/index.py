import streamlit as st

from streamlit.server.server import Server

st.header("Index")

app_files = Server.get_current().get_app_files()
for file_path in app_files:
    st.markdown(
        f'<a href="{file_path}" target="_self">{file_path}</a>', unsafe_allow_html=True
    )
