import streamlit as st
import requests
from model_helper import predict  # optional (see note below)

API_URL = "https://car-damage-detection-m.onrender.com/predict"

st.title("🚗 Car Damage Detection")

uploaded_file = st.file_uploader(
    "Upload the image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Show uploaded image
    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    # ---------- CALL BACKEND API ----------
    files = {
        "file": uploaded_file.getvalue()
    }

    with st.spinner("Analyzing damage..."):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success("Prediction from Backend")
        st.json(result)
    else:
        st.error("❌ Backend error")

    # ---------- OPTIONAL: LOCAL PREDICTION ----------
    # (REMOVE this block if backend already does ML)
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    local_prediction = predict(image_path)
    st.info(f"Local Prediction: {local_prediction}")
