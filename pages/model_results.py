import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def app():
    st.title("Model Training & Evaluation")

    df = pd.read_csv('data/Retail_Inventory_Data.csv')
    df['Order_Demand'] = df['Order_Demand'].apply(lambda x: -int(x) if '-' in x else int(x))
    df['high_demand'] = df['Order_Demand'].apply(lambda x: 1 if x > df['Order_Demand'].median() else 0)

    df.drop(['Order_Demand', 'Date'], axis=1, inplace=True)
    df.fillna('unknown', inplace=True)

    for col in df.select_dtypes(include='object').columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop('high_demand', axis=1)
    y = df['high_demand']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Naive Bayes
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    nb_acc = accuracy_score(y_test, nb.predict(X_test))

    # KNN
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    knn_acc = accuracy_score(y_test, knn.predict(X_test))

    st.write(f"Naive Bayes Accuracy: {nb_acc:.2f}")
    st.write(f"KNN Accuracy: {knn_acc:.2f}")

