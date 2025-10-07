import streamlit as st
from PIL import Image

st.set_page_config(page_title="图片转ASCII画", page_icon="")

st.title("图片转ASCII画")
st.write("上传一张图片，自动生成ASCII画！")

uploaded_file = st.file_uploader("选择一张图片，后缀名要为.jpg", type=["jpg"])

if uploaded_file is not None:
    ascii_chars = list("@#S%?*+;:,. ")
    img = Image.open(uploaded_file)
    w_percent = 150 / float(img.size[0])
    height = int(float(img.size[1]) * float(w_percent * 0.5))
    img = img.resize((150, height), Image.NEAREST)
    img = img.convert("L")
    pixels = img.load()
    result = ""
    for i in range(height):
        for j in range(150):
            gray = pixels[j, i]
            index = int(gray / 23)
            result += ascii_chars[index]
        result += "\n"
   
    st.text(result)