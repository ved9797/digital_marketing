import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from PIL import Image # This is for image display
import google.generativeai as genai

# Configure the key and initiate the model
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Create the front end of the application here
st.header("🧠Textify Snap- :blue[Image in, textified out!]",divider = True)
prompt = st.text_input("Enter the Prompt")

# File uploader section
uploaded_img = st.file_uploader("Upload an Image",type=["jpg","jpeg","png"])

# Display the uploaded image
image = ""
if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image,use_container_width=True)

def img_and_prompt(image,prompt):
    if prompt!="":
        response = model.generate_content([prompt,image])
    else:
        response = model.generate_content([prompt])  
    return response.text

# Submit
submit = st.button("🚀 Submit")
if submit:
    response = img_and_prompt(prompt,image)
    st.subheader(":orange[Response:]")
    st.markdown(response)
