
import streamlit as st
import requests

API_URL = "http://16.171.30.124:8000/predict"

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Inputs
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job',
     'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        with st.spinner("Calling API..."):
            response = requests.post(API_URL, json=input_data, timeout=30)

        # Debug info (VERY IMPORTANT for fixing issues)
        st.write("Status Code:", response.status_code)
        st.write("Raw Response:", response.text)

        # Try parsing JSON safely
        try:
            result = response.json()
        except Exception:
            st.error("Invalid JSON response from API")
            st.stop()

        # Handle multiple possible API formats
        data = result.get("response", result)

        predicted_category = data.get("predicted_category", "N/A")
        confidence = data.get("confidence", None)
        class_probs = data.get("class_probabilities", None)

        # Output
        st.success(f"Predicted Category: {predicted_category}")

        if confidence is not None:
            st.write("🔍 Confidence:", confidence)

        if class_probs is not None:
            st.write("📊 Class Probabilities:")
            st.json(class_probs)

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to FastAPI server")

    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out")

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")