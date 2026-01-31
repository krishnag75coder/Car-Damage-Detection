import streamlit as st
import requests

# Access secrets
API_URL = st.secrets["api_keys"]["fastapi_url"]
db_user = st.secrets["database"]["user"]
db_pass = st.secrets["database"]["password"]

st.title("Car Damage Detection")

uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

if uploaded_file:
    # Proper multipart format for FastAPI
    files = {"file": ("image.jpg", uploaded_file.getvalue(), uploaded_file.type)}

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        # Show backend error detail if available
        try:
            st.error(response.json().get("detail", "Backend error"))
        except:
            st.error("Backend error (non-JSON response)")

# Optional: show database info (just for testing, normally don't display passwords)
st.write(f"DB User: {db_user}")
