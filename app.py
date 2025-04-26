import streamlit as st
import pandas as pd
import numpy as np
import random

# --- Page config ---
st.set_page_config(page_title="Australian House Price Predictor 🏡", layout="centered")

# --- Title ---
st.title("🏡 Australian House Price Predictor & Suburb Recommender")
st.write("Find your dream suburb based on your budget, room preferences, and lifestyle needs in Australia!")

# --- Suburbs List ---
suburbs = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Hobart", "Darwin"]

# --- User Inputs ---
st.header("🔎 Search Filters")
col1, col2 = st.columns(2)

with col1:
    suburb = st.selectbox("Choose a Suburb", suburbs)
    rooms = st.slider("Select Number of Bedrooms", 1, 6)
    budget = st.slider("Your Budget (AUD)", 300000, 2000000, step=50000)
    
with col2:
    near_transport = st.checkbox("🚉 Require Public Transport Nearby?")
    pet_friendly = st.checkbox("🐶 Pet Friendly Housing?")
    low_crime = st.checkbox("🛡️ Prefer Low Crime Area?")

# --- Simulate a prediction ---
st.header("🏠 Your Results")

# Fake logic to simulate price prediction
base_price = random.randint(400000, 1200000)
price_adjustment = rooms * 25000
location_factor = suburbs.index(suburb) * 30000
feature_bonus = 0

if near_transport:
    feature_bonus += 20000
if pet_friendly:
    feature_bonus += 15000
if low_crime:
    feature_bonus += 25000

predicted_price = base_price + price_adjustment + location_factor + feature_bonus

# --- Show prediction ---
st.subheader(f"Predicted House Price in {suburb}:")
st.success(f"Around **${predicted_price:,.0f} AUD** 🏡")

# --- Recommend if fits budget ---
if predicted_price <= budget:
    st.balloons()
    st.success(f"🎯 Great choice! This property fits your budget of **${budget:,.0f} AUD**.")
else:
    st.warning(f"⚡ Oops! You might need to increase your budget by about **${predicted_price - budget:,.0f} AUD**.")

# --- Summary Tips ---
st.header("💡 Summary Tips")
if near_transport and pet_friendly and low_crime:
    st.info("✅ You prefer a premium lifestyle! Expect slightly higher prices but great quality living.")
elif not (near_transport or pet_friendly or low_crime):
    st.info("🔍 No special preferences selected. You might find cheaper deals!")

# --- Footer ---
st.write("---")
st.caption("Made with ❤️ for the Australian Data Science Market!")

