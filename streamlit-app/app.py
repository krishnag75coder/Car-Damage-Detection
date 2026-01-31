import streamlit as st
from model_helper import predict

st.title("Car Damage Detection")
uploaded_file = st.file_uploader("Upload the image",type=["png","jpg","jpeg"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(image_path, caption="Uploaded Image", width='stretch')
        prediction = predict(image_path)
        st.info(f"Prediction: {prediction}")
