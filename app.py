import streamlit as st 
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv() 

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Input prompt for Gemini
input_prompt = """
You are a nutrition expert. Based on the provided food image, identify the food items and estimate the approximate number of calories for each item, followed by the total calorie count.

Output format:
- Item 1: [Food Name] – [Estimated Calories] kcal
- Item 2: ...
- Total: [Total Calories] kcal

Be concise and accurate, also give feedback if the food is healdy or not. 

"""

# Function to format image for Gemini API
def input_image_setup(uploaded_file):
    if uploaded_file is not None: 
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to call Gemini API
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input, image[0]])
    return response.text

# ----------------------------------
# ✅ Streamlit App UI starts here!
# ----------------------------------

st.set_page_config(page_title="Calorie Counter AI")
st.title("Calorie Counter AI")

uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None: 
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Generate Results")

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("🥦 Estimated Calories & Nutritional Info")
    st.write(response)
