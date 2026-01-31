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

    # Correct multipart format for FastAPI
    files = {
        "file": ("image.jpg", uploaded_file.getvalue(), uploaded_file.type)
    }

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, files=files)

    st.write("Status Code:", response.status_code)
    st.write("Response Text:", response.text)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        # Show backend error detail
        try:
            st.error(response.json().get("detail", "Backend error"))
        except:
            st.error("Backend error (non-JSON response)")
