import streamlit as st
import requests

st.title("Car Damage Detection")

uploaded_file = st.file_uploader(
    "Upload the image",
    type=["png", "jpg", "jpeg"]
)

API_URL = "https://car-damage-detection-m.onrender.com/predict"

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    files = {
        "file": uploaded_file.getvalue()
    }

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error("Backend error")
