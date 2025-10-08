import streamlit as st
from PIL import Image

st.set_page_config(page_title="图片转ASCII画", page_icon="")

st.markdown("""
<style>
.pre-standard {
    overflow-x: auto;
    white-space: pre;
    font-family: sans-serif;
    font-size: 10px;
}
.pre-mono {
    overflow-x: auto;
    white-space: pre;
    font-family: 'Courier New', Courier, monospace;
    font-size: 10px;
    line-height: 10px;
}
</style>
""", unsafe_allow_html=True)

if st.button("🔧 点我切换等宽字体（防拉伸）"):
    st.session_state.use_mono = True
use_mono = st.session_state.get("use_mono", False)

st.title("图片转ASCII画")
st.write("上传一张图片，自动生成ASCII画！")

uploaded_file = st.file_uploader("选择一张图片，后缀名要为.jpg", type=["jpg"])

cols = st.number_input("输出宽度（字符数）", min_value=10, max_value=300, value=150, step=2)

if uploaded_file is not None:
    ascii_chars = list("@#S%?*+;:,. ")
    img = Image.open(uploaded_file)
    w_percent = cols / float(img.size[0])
    height = int(float(img.size[1]) * float(w_percent * 0.5))
    img = img.resize((cols, height), Image.NEAREST)
    img = img.convert("L")
    pixels = img.load()
    result = ""
    for i in range(height):
        for j in range(cols):
            gray = pixels[j, i]
            index = int(gray / 23)
            result += ascii_chars[index]
        result += "\n"
    pre_class = "pre-mono" if use_mono else "pre-standard"
    st.markdown(f"<pre class='{pre_class}'>{result}</pre>", unsafe_allow_html=True)
