import streamlit as st
import pandas as pd
import pickle

def app():
    st.title("Demand Prediction Form")

    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)

    st.subheader("Input Features")
    st.write("Isi nilai fitur sesuai data yang dimiliki")

    feature1 = st.number_input("Feature 1 (e.g., Product_Category)", min_value=0)
    feature2 = st.number_input("Feature 2 (e.g., Warehouse)", min_value=0)
    feature3 = st.number_input("Feature 3 (e.g., SKU ID)", min_value=0)

    if st.button("Predict"):
        prediction = model.predict([[feature1, feature2, feature3]])
        st.success(f"Prediksi permintaan tinggi: {'Ya' if prediction[0] == 1 else 'Tidak'}")

