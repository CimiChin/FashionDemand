class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        import streamlit as st
        app = st.sidebar.selectbox("Select Page", self.apps, format_func=lambda app: app["title"])
        app["function"]()

