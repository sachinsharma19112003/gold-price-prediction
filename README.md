# 📈 Gold Price Prediction App

Predict future gold prices using historical **Open, High, and Low** price data with a machine learning model. This app is built using **Python** and **Streamlit**, making it easy to interactively forecast gold prices without any complex setup.

---

## 🔹 Features

* Predict gold prices based on:

  * Open Price
  * High Price
  * Low Price
* Two input methods:

  1. **Manual Input** – Enter prices manually.
  2. **CSV Upload** – Upload a CSV file with historical price data.
* User-friendly interface with **Streamlit**.
* Real-time predictions and results visualization.

---

## 🛠️ Tech Stack

* **Python** – Main programming language
* **Streamlit** – Web app UI
* **scikit-learn** – Machine Learning model
* **pandas & numpy** – Data handling
* **joblib** – Model saving and loading

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gold-price-prediction.git
cd gold-price-prediction
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

---

## 📂 Input Data

* **Manual Input:** Enter Open, High, Low prices manually in the app.
* **CSV Input:** CSV should contain columns:

| Open | High | Low  |
| ---- | ---- | ---- |
| 1950 | 1980 | 1940 |

---

## 📈 Example Prediction

* Input:

  * Open: 1950
  * High: 1980
  * Low: 1940
* Predicted Gold Price: **1975.32**

---

## 📝 File Structure

```
gold-price-prediction/
│
├─ app.py             # Main Streamlit app
├─ gold_model.pkl     # Trained ML model
├─ scaler.pkl         # Scaler used for preprocessing
├─ requirements.txt   # Dependencies
├─ README.md          # Project documentation
└─ data/              # Example CSV files
```

---

## ⚡ Requirements

`requirements.txt` should contain:

```
streamlit
numpy
pandas
scikit-learn
joblib
```

---

## 💡 Future Enhancements

* Add **time-series forecasting** for future prices.
* Integrate **visualizations** like trend charts.
* Deploy the app on **Heroku** or **Streamlit Cloud**.
* Add support for multiple metals (Silver, Platinum, etc.).

---

## 📞 Contact

Created by **Sachin Sharma** – Data Scientist 
GitHub: [https://github.com/sachinsharma19112003/gold-price-prediction]
deploy :https://gold-price-prediction-wunlk6ka6wfndmx9qjhxpw.streamlit.app/
