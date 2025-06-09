# Fashion Demand Prediction Dashboard

This Streamlit project is a multi-page dashboard for predicting fashion product demand using machine learning models.

## 🔍 Project Overview

This dashboard has three main pages:

1. **EDA & Dataset**: Display the dataset with descriptive statistics and visualizations.
2. **Model Results**: Train and evaluate Naive Bayes and KNN classifiers.
3. **Predict Demand**: A form to input new product data and predict whether the demand will be high.

## 📊 Dataset

The dataset used is from Kaggle:
[Retail Store Inventory Forecasting Dataset](https://www.kaggle.com/datasets/anirudhchauhan/retail-store-inventory-forecasting-dataset)

## ⚙️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/fashion-demand-dashboard.git
cd fashion-demand-dashboard
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Download the dataset** and place it in the `data/` folder.

4. **Train the model and save it**:
   Run the model training script (provided in the documentation) to generate `models/model.pkl`.

5. **Run the app**:

```bash
streamlit run app.py
```

## 🧠 Models Used

* Naive Bayes (GaussianNB)
* K-Nearest Neighbors (KNN)

## 📁 Folder Structure

```
.
├── app.py
├── multiapp.py
├── requirements.txt
├── data/
│   └── Retail_Inventory_Data.csv
├── models/
│   └── model.pkl
├── pages/
│   ├── eda.py
│   ├── model_results.py
│   └── prediction.py
```

## 📌 Note

* This app predicts whether the product demand is **high** or **low** based on features.
* Preprocessing includes label encoding and binary classification on `Order_Demand`.

## ✅ To Do

* Add more model options
* Improve UI with custom CSS or Streamlit components

---

Created for educational purposes and practical M
