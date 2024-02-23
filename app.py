from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import matplotlib.pyplot as plt

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input, image, prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

##initialize our streamlit app

st.set_page_config(page_title=" GeminAI HealthCare Assistance mini🎄")

# Custom CSS for heading
st.markdown(
    """
    <style>
    .big-heading {
        color: #FFD700;
        font-size: 36px;
        font-weight: bold;
        padding-top: 20px;
        padding-bottom: 20px;
    }
    .horizontal-box {
        background-color: #4CAF50;
        border: none;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        padding: 10px 20px;
        width: fit-content;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Big heading with green apple symbol
st.markdown('<p class="big-heading">GeminAI HealthCare Assistance mini🎄</p>', unsafe_allow_html=True)

# Upload image and explore insights box
st.markdown('<p class="horizontal-box">Upload Image Explore Insights</p>', unsafe_allow_html=True)

# Sidebar with images and headings
st.sidebar.title("🍽️ Food Info")
#st.sidebar.image("your_image1.jpg", width=100)
#st.sidebar.image("your_image2.jpg", width=100)
#st.sidebar.image("your_image3.jpg", width=100)
st.sidebar.header("Try Your Free Health Assistance")
st.sidebar.header("Upload any Food images")
st.sidebar.header("Look the Magic")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
input = st.text_input("Input Prompt: ", key="input")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)




# Custom CSS for the star-shaped box
st.markdown(
    """
    <style>
    .star-box {
        width: 250px;
        height: 300px;
        background: linear-gradient(-45deg, #008080, #800080, #008080);
        border-radius: 25px;
        padding: 20px;
        color: white;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Text inside the star-shaped box
st.sidebar.markdown('<div class="star-box">Welcome to our HealthCare App! To get started, simply upload an image of your food. Once uploaded, feel free to ask any questions related to the food item. Our AI will provide insights on nutrition, calories, and preparation methods. Enjoy exploring!</div>', unsafe_allow_html=True)



    
# Custom CSS for cartoon buttons
st.markdown(
    """
    <style>
    .cartoon-button {
        background-color: #ffd700;
        border: none;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 50%;
        width: 60px;
        height: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

## If submit button is clicked
try:
    if st.button("🍲 Total calories", key="calories"):
        image_data = input_image_setup(uploaded_file)
        input_prompt = """
            You are an expert in nutritionist where you need to see the food items from the image
            and calculate the total calories, also provide the details of every food item with calories intake
            as below format:
            
            1. Item 1 - no of calories
            2. Item 2 - no of calories
            ----
            ----
        """
        response = get_gemini_repsonse(input, image_data, input_prompt)
        st.subheader("Total Calories")
        st.write(response)
        
        # Example bar chart for total calories
        # You can replace this with your actual data
        #calories_data = {
          #  "Item 1": 300,
           # "Item 2": 500,
           # "Item 3": 200
       # }
      #  plt.bar(calories_data.keys(), calories_data.values())
     ##   plt.ylabel("Calories")
       # st.pyplot(plt)
except FileNotFoundError as e:
    st.error(f"Error: {e}")

try:
    if st.button("👩‍🍳 Preparation Method", key="preparation"):
        image_data = input_image_setup(uploaded_file)
        input_prompt = """
            You are an expert in nutritionist where you need to see the food items from the image
            and give points how to make that dish also some healthy tips.
            
            ----
            ----
        """
        response = get_gemini_repsonse(input, image_data, input_prompt)
        st.subheader("Preparation Method")
        st.write(response)
except FileNotFoundError as e:
    st.error(f"Error: {e}")

try:
    if st.button("🥦 Nutrition content", key="nutrition"):
        image_data = input_image_setup(uploaded_file)
        input_prompt = """
            You are an expert in nutritionist where you need to see the food items from the image
            and give points wise how much vitamins, nutrients, fat, and so on are present in each item of the food like this:

            a.Name or heading
            
            1. Groundnut
            2.zinc = 20% per gram
            3.carbohydrates = 33% per gram
            4.vitamins per gram


            b.Name or heading

            1. Groundnut   
            2.zinc = 20% per gram
            3.carbohydrates = 33% per gram
            4.vitamins per gram


            ----
            ----
        """
        response = get_gemini_repsonse(input, image_data, input_prompt)
        st.subheader("Nutritional Content")
        st.write(response)
except FileNotFoundError as e:
    st.error(f"Error: {e}")
