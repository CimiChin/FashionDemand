import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Exploratory Data Analysis")
    df = pd.read_csv('data/Retail_Inventory_Data.csv')

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Info")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Visualisasi Permintaan")
    fig, ax = plt.subplots()
    sns.histplot(df['Order_Demand'].apply(lambda x: -int(x) if '-' in x else int(x)), bins=50, ax=ax)
    st.pyplot(fig)

