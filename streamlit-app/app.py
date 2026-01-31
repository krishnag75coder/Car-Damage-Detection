import streamlit as st
from model_helper import predict
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Car Damage Detection 🚗",
    page_icon="🚘",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better design
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #FF7878;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("🚗 Car Damage Detection System")
st.markdown("Upload an image of your car and let the AI detect the type of damage.")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

# Predict button
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict Damage"):
        # Save temporary image
        image_path = "temp_file.jpg"
        image.save(image_path)

        # Get prediction
        with st.spinner("Analyzing image..."):
            prediction = predict(image_path)
        st.success(f"Prediction: {prediction}")
