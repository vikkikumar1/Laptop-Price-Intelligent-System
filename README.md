# 💻 Laptop Price Predictor 

An end-to-end Machine Learning project that predicts laptop prices based on specifications.

---

## 🚀 Features

- Machine Learning model (Random Forest)
- Feature engineering (PPI, CPU, Memory parsing)
- FastAPI backend (REST API)
- Streamlit frontend (interactive UI)
- Deployed on Render

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit

---

## 📊 Input Features

- Company
- Type
- RAM
- Weight
- Touchscreen
- IPS
- PPI
- CPU
- HDD (GB)
- SSD (GB)
- GPU
- OS

---

## 🌐 Live Demo

- 🔗 API: https://laptop-price-api-dwz3.onrender.com/docs
- 🔗 App: https://vikkikumar1-laptop-price-intelligent-system-frontendapp-emjqsi.streamlit.app/

---

## ⚙️ Run Locally


### 1️⃣ Clone the repository

```bash
git clone https://github.com/vikkikumar1/Laptop-Price-Intelligent-System.git
cd Laptop-Price-Intelligent-System
```

---

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the model (optional if .pkl exists)

```bash
python model/train.py
```

---

### 5️⃣ Run FastAPI backend

```bash
uvicorn app.main:app --reload
```

👉 API will run at:
http://127.0.0.1:8000/docs

---

### 6️⃣ Run Streamlit frontend

```bash
cd frontend
streamlit run app.py
```

👉 App will run at:
http://localhost:8501
