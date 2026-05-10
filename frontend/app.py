import streamlit as st
import pandas as pd
import requests
import os

# ================= CONFIG =================
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# 🔴 REPLACE THIS WITH YOUR ACTUAL RENDER API URL
API_URL = "https://laptop-price-api-dwz3.onrender.com/predict"

# ================= LOAD DATA =================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@st.cache_data
def load_data():
    return pd.read_csv(os.path.join(BASE_DIR, 'data', 'laptop_data.csv'))

df = load_data()

# ================= UI =================
st.title("💻 Laptop Price Predictor")
st.write("🌐 Powered by FastAPI Backend")

# ================= INPUT =================

company = st.selectbox('Brand', df['Company'].unique())
type_name = st.selectbox('Type', df['TypeName'].unique())

ram = st.selectbox('RAM (GB)', [4, 8, 16, 32, 64])
weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5)

touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# ✅ Direct PPI input
ppi = st.number_input(
    'PPI (Pixels Per Inch)',
    min_value=50.0,
    max_value=500.0,
    value=150.0
)

st.caption("💡 Typical PPI: 100–300 (higher = sharper display)")

# ✅ MUST match training columns
cpu = st.selectbox('CPU', df['Cpu brand'].unique())
gpu = st.selectbox('GPU', df['Gpu'].apply(lambda x: x.split()[0]).unique())
os_type = st.selectbox('Operating System', df['OpSys'].unique())

hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024])
ssd = st.selectbox('SSD (GB)', [0, 128, 256, 512, 1024])

# ================= PREDICTION =================

if st.button('Predict Price'):

    # Convert categorical inputs
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Prepare data for API
    data = {
        "company": company,
        "type": type_name,
        "ram": ram,
        "weight": weight,
        "touchscreen": touchscreen_val,
        "ips": ips_val,
        "ppi": ppi,
        "cpu": cpu,
        "hdd": hdd,
        "ssd": ssd,
        "gpu": gpu,
        "os": os_type
    }

    try:
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            result = response.json()
            price = result.get("predicted_price", None)

            if price:
                st.success(f"💰 Estimated Price: ₹ {price}")
            else:
                st.error("❌ Unexpected API response format")

        else:
            st.error(f"❌ API Error: {response.status_code}")

    except Exception as e:
        st.error("❌ Could not connect to API. Please check backend deployment.")