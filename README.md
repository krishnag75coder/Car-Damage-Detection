# 🚗 Car Damage Detection System

## 🔗 Live Links
- Frontend (Streamlit): https://car-damage-detection-cczfsvpibec4ozjwbffxud.streamlit.app/
- Backend API (Render): https://car-damage-detection-m.onrender.com/

## 📌 Project Overview
An end-to-end deep learning-based system that detects car damage severity from images using a deployed ML model.

## 🧠 Tech Stack
- Frontend: Streamlit
- Backend: FastAPI / Flask
- ML: Pytorch
- Deployment: Streamlit Community Cloud, Render
- Language: Python

## ⚙️ Architecture
Streamlit UI → FastAPI Backend → ML Model → Prediction Response

## 📂 Features
- Upload car damage image
- Real-time prediction
- Cloud-deployed ML inference
- REST API support

## 🚀 API Endpoints
POST /predict  
Input: Image file  
Output: Damage classification

## 🧪 How to Run Locally
```bash
pip install -r requirements.txt
python main.py
streamlit run app.py

