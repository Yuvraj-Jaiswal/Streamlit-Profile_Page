import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="Profile Page" , page_icon=":tada:" , layout="wide" )

#0E1117
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:return None
    return r.json()

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

load_css("style/style.css")

lottie_coding = load_lottie("https://assets8.lottiefiles.com/packages/lf20_vnikrcia.json")
lottie_contact = load_lottie("https://assets8.lottiefiles.com/packages/lf20_isbiybfh.json")
mask_file = open('videos/Mask_detector.mp4', 'rb') #enter the filename with filepath
video_mask = mask_file.read()

bloodcell_file = open('videos/BloodCell_Detector.mp4', 'rb') #enter the filename with filepath
video_bloodcell = bloodcell_file.read()

Img_Digit1 = Image.open("images/gen1.png")
Img_Digit2 = Image.open("images/gen2.png")
Img_Digit3 = Image.open("images/gen3.png")

Img_Color1 = Image.open("images/color1.png")
Img_Color2 = Image.open("images/color2.png")
Img_Color3 = Image.open("images/color3.png")

Img_Res1 = Image.open("images/res1.png")
Img_Res2 = Image.open("images/res2.png")

with st.container():
    st.subheader("Hi i am Yuvraj Jaiswal :wave:")
    st.title("I am passionate about machine Leaning and Deep learning.")
    st.subheader("I am fluent in python , c++ programming laguages.")
    st.write("[My github projects link](https://github.com/Yuvraj-Jaiswal)")

with st.container():
    st.write("---")
    left_col , right_col = st.columns((2,1))
    with left_col:
        st.header("My prominent skills")
        st.write("##")
        st.write("""
        - I am fluent in python , c++ and kotlin programming laguages.
        - I am also fluent in web development laguages and frameworks like HTML5 , CSS , Javascript and Bootstrap.
        - I am 5 star in hackerrank algorithm section.
        - I had made countless Deeplearning and Machine learning projects.
        - Worked on Object Detection , Generative Neural Networks , Convolutional Neural Networks , Recurrent Neural Networks , Reinforcement Learning and many more fields.
        - With technical skills i also have excellent communication skills. 
        """)
    with right_col:
        st.write("")
        st_lottie(lottie_coding,height=300,key="coding")

with st.container():
    st.write("---")
    st.header("Some of my projects")
    st.write("##")
    left_col, right_col = st.columns((1, 1))
    with left_col:
        st.subheader("- Mask Detector")
        st.video(mask_file)
    with right_col:
        st.subheader("- BloodCell Detector")
        st.video(bloodcell_file)

with st.container():
    st.write("##")
    st.subheader("- Digit Generation ( Generative Neural Network )")
    left_col, middle_col , right_col = st.columns((1, 1, 1))
    with left_col:
        st.image(Img_Digit1,use_column_width=True)
    with middle_col:
        st.image(Img_Digit2,use_column_width=True)
    with right_col:
        st.image(Img_Digit3,use_column_width=True)

with st.container():
    st.write("##")
    st.subheader("- Image Colorization ( Deep Neural Network )")
    left_col, middle_col , right_col = st.columns((1, 1, 1))
    with left_col:
        st.image(Img_Color1)
    with middle_col:
        st.image(Img_Color2)
    with right_col:
        st.image(Img_Color3)

with st.container():
    st.write("##")
    st.subheader("- Image SuperResolution ( Deep Neural Network )")
    left_col, right_col = st.columns((1, 1))
    with left_col:
        st.image(Img_Res1)
    with right_col:
        st.image(Img_Res2)


with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/yuvrajjaiswal1632@gmail.COM" method="POST">
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
        st_lottie(lottie_contact,height=270,quality="medium")
        st.write("")