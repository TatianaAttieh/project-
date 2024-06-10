from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Updated the CSS file path
local_css(r".\style\style.css")

lottie_code = load_lottieurl("https://lottie.host/f4e1ee57-7e70-4a2f-9d43-095e13dcfc3a/dIhexjlzjO.json")

# Define the path to the image
image_path = r".\images\img 1.PNG"

# Initialize img_lottie_animation to None
img_lottie_animation = None

# Check if the file exists and load the image if it does
if os.path.exists(image_path):
    try:
        img_lottie_animation = Image.open(image_path)
    except Exception as e:
        st.error(f"Error loading image: {e}")
else:
    st.error(f"Image not found at {image_path}")

# HEADER
with st.container():
    st.subheader("Hi, I am Tatiana :wave:")
    st.title("A Data Analyst From Lebanon")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficace")
    st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

    with right_column:
        st_lottie(lottie_code, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it. In this tutorial, I'll show you exactly how to do it.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSO1tGoINE)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/codingisfun.testuser@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

