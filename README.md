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

- 🔗 API: https://your-app.onrender.com/docs
- 🔗 App: https://your-streamlit-link

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/project.git
cd project
pip install -r requirements.txt

# Train model
python model/train.py

# Run API
uvicorn app.main:app --reload

# Run UI
cd frontend
streamlit run app.py