import streamlit as st
import base64
import os

st.set_page_config(page_title="리뷰 이벤트 안내판", layout="centered")

def get_base64(file):
    return base64.b64encode(file).decode()

img_src = ""
uploaded_file = st.file_uploader("QR코드 이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    img_src = f"data:image/png;base64,{get_base64(uploaded_file.read())}"
else:
    file_path = "KakaoTalk_20260311_133707826.png"
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            img_src = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    else:
        img_src = "https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=example"

# Streamlit 에러 방지를 위해 모든 들여쓰기를 제거한 최종 코드입니다.
html_code = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
#MainMenu {{visibility: hidden;}} header {{visibility: hidden;}} footer {{visibility: hidden;}}
.block-container {{padding: 2rem 1rem; max-width: 500px; background-color: #1a1a1a;}}
.card {{
font-family: 'Noto Sans KR', sans-serif;
background: linear-gradient(145deg, #222, #111);
border: 2px solid #c5a059;
border-radius: 25px;
padding: 40px 20px;
text-align: center;
color: white;
box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}}
.title {{ color: #c5a059; font-size: 2.2rem; font-weight: 900; margin-bottom: 10px; }}
.subtitle {{ font-size: 1.1rem; margin-bottom: 30px; line-height: 1.4; color: #ddd; }}
.qr-box {{ 
background: white; padding: 15px; display: inline-block; 
border-radius: 15px; margin-bottom: 25px; border: 4px solid #333;
}}
.qr-box img {{ width: 200px; height: 200px; display: block; }}
.steps {{ 
text-align: left; background: rgba(255,255,255,0.05); 
padding: 20px; border-radius: 15px; margin-bottom: 25px; 
}}
.step {{ display: flex; align-items: center; margin-bottom: 12px; font-size: 1rem; }}
.num {{ 
background: #c5a059; color: #111; width: 24px; height: 24px; 
border-radius: 50%; display: flex; justify-content: center; 
align-items: center; font-weight: bold; margin-right: 12px; flex-shrink: 0;
}}
.reward {{ 
background: #c5a059; color: #111; padding: 15px; 
border-radius: 10px; font-weight: 900; font-size: 1.2rem; 
}}
</style>

<div class="card">
<div class="title">방문자 리뷰 EVENT!!</div>
<div class="subtitle">플레이스 저장하고 리뷰 남겨주시면<br><b>100% 서비스 당첨</b></div>
<div class="qr-box">
<img src="{img_src}">
</div>
<div class="steps">
<div class="step"><div class="num">1</div>QR코드 스캔</div>
<div class="step"><div class="num">2</div>네이버 플레이스 '저장' 클릭</div>
<div class="step"><div class="num">3</div>방문자 리뷰 작성</div>
<div class="step"><div class="num">4</div>직원에게 리뷰 화면 보여주세요</div>
</div>
<div class="reward">음료 / 서비스 / 할인 100% 제공</div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
