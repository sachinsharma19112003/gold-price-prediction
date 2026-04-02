import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ------------------------------
# Load trained model and scaler
# ------------------------------
model = joblib.load("gold_model.pkl")
scaler = joblib.load("scaler.pkl")

# ------------------------------
# Streamlit App
# ------------------------------
st.set_page_config(page_title="Gold Price Predictor", page_icon="💰")
st.title("💰 Gold Price Prediction App")
st.write("Predict gold prices by entering Open, High, and Low values.")

# ------------------------------
# Input values
# ------------------------------
open_price = st.number_input("Open Price", min_value=0.0, value=5000.0, step=1.0)
high_price = st.number_input("High Price", min_value=0.0, value=5050.0, step=1.0)
low_price = st.number_input("Low Price", min_value=0.0, value=4950.0, step=1.0)

# ------------------------------
# Predict button
# ------------------------------
if st.button("Predict Gold Price"):
    # Validate realistic inputs
    if open_price <= 0 or high_price <= 0 or low_price <= 0:
        st.warning("Please enter positive values close to actual gold prices!")
    elif low_price > high_price or open_price > high_price or open_price < low_price:
        st.warning("Please enter realistic values: Low ≤ Open ≤ High")
    else:
        # Prepare input and scale
        X_new = np.array([[open_price, high_price, low_price]])
        X_new_scaled = scaler.transform(X_new)

        # Predict
        prediction = model.predict(X_new_scaled)
        st.success(f"Predicted Gold Price: {prediction[0]:.2f} 💰")
