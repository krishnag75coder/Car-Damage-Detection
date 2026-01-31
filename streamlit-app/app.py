import streamlit as st
import requests

st.title("🚗 Car Damage Detection")

API_URL = "https://car-damage-detection-m.onrender.com/predict"

uploaded_file = st.file_uploader(
    "Upload the image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict Damage"):
        with st.spinner("Analyzing image..."):
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:
                response = requests.post(API_URL, files=files, timeout=60)

                if response.status_code == 200:
                    result = response.json()

                    prediction = result.get("prediction", "Unknown")
                    confidence = result.get("confidence")

                    st.success(f"Prediction: **{prediction}**")

                    if confidence is not None:
                        st.info(f"Confidence: **{confidence:.2f}**")
                else:
                    st.error(f"Backend error: {response.text}")

            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
