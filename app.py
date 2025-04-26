# app.py
!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
df.rename(columns={'medv': 'Price', 'lstat': 'CrimeRate', 'rm': 'Rooms', 'dis': 'DistanceToCBD'}, inplace=True)
df = df[['Price', 'CrimeRate', 'Rooms', 'DistanceToCBD']]

# Train model
X = df[['CrimeRate', 'Rooms', 'DistanceToCBD']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit app
st.title("🏡 Australian House Price Predictor & Suburb Recommender")

st.sidebar.header("Set Your Preferences")
budget = st.sidebar.slider('Your Budget (in $1000s)', 10, 50, 30)
min_rooms = st.sidebar.slider('Minimum Rooms', 2, 8, 4)
max_crime_rate = st.sidebar.slider('Maximum Crime Rate (%)', 1, 30, 10)
max_distance = st.sidebar.slider('Max Distance to CBD (km)', 1, 12, 5)

if st.sidebar.button("Find Suburbs"):
    suitable_houses = df[
        (df['Price'] <= budget) & 
        (df['Rooms'] >= min_rooms) & 
        (df['CrimeRate'] <= max_crime_rate) & 
        (df['DistanceToCBD'] <= max_distance)
    ]
    
    if suitable_houses.empty:
        st.error("No suburbs match your preferences 😔")
    else:
        st.success(f"🏘️ {len(suitable_houses)} suburbs found matching your criteria!")
        st.dataframe(suitable_houses.sort_values('Price'))

st.write("---")
st.subheader("📊 Data Overview")
st.dataframe(df.head())
