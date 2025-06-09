# app.py
import streamlit as st
from multiapp import MultiApp
from pages import eda, model_results, prediction

app = MultiApp()

app.add_app("EDA & Dataset", eda.app)
app.add_app("Model Results", model_results.app)
app.add_app("Predict Demand", prediction.app)

app.run()

