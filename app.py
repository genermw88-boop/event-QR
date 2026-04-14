import streamlit as st
import base64

st.set_page_config(page_title="리뷰 이벤트 안내판", layout="centered")

# 기본 임시 이미지
img_src = "https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=example"

# 1. 파일 업로드 기능
uploaded_file = st.file_uploader("여기를 눌러 사장님의 QR코드 이미지를 올려주세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 버그 해결: read() 대신 getvalue()를 사용하여 화면이 새로고침 되어도 이미지가 유지되도록 수정
    file_bytes = uploaded_file.getvalue()
    encoded_b64 = base64.b64encode(file_bytes).decode()
    img_src = f"data:image/png;base64,{encoded_b64}"

# 2. 안내판 디자인 및 다운로드 스크립트 (들여쓰기 제거 완료)
html_code = f"""
<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
#MainMenu {{visibility: hidden;}} header {{visibility: hidden;}} footer {{visibility: hidden;}}
.block-container {{padding: 1rem; max-width: 500px; background-color: #1a1a1a;}}
.card-wrapper {{ padding: 20px; display: flex; flex-direction: column; align-items: center; }}
.card {{
font-family: 'Noto Sans KR', sans-serif;
background: linear-gradient(145deg, #222, #111);
border: 2px solid #c5a059;
border-radius: 25px;
padding: 40px 20px;
text-align: center;
color: white;
width: 100%;
max-width: 400px;
box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}}
.title {{ color: #c5a059; font-size: 2.2rem; font-weight: 900; margin-bottom: 10px; }}
.subtitle {{ font-size: 1.1rem; margin-bottom: 30px; line-height: 1.4; color: #ddd; }}
.qr-box {{ 
background: white; padding: 15px; display: inline-block; 
border-radius: 15px; margin-bottom: 25px; border: 4px solid #333;
}}
.qr-box img {{ width: 200px; height: 200px; display: block; object-fit: contain; }}
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
.download-btn {{
margin-top: 20px;
background-color: #c5a059;
color: black;
border: none;
padding: 12px 24px;
border-radius: 8px;
font-weight: bold;
cursor: pointer;
font-size: 1rem;
}}
.download-btn:hover {{ background-color: #e2bd78; }}
</style>

<div class="card-wrapper">
<div class="card" id="notice-board">
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
<button class="download-btn" onclick="downloadImage()">이미지로 저장하기 (PNG)</button>
</div>

<script>
function downloadImage() {{
    const board = document.getElementById('notice-board');
    html2canvas(board, {{
        backgroundColor: "#1a1a1a",
        scale: 2
    }}).then(canvas => {{
        const link = document.createElement('a');
        link.download = '리뷰이벤트_안내판.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    }});
}}
</script>
"""

st.markdown(html_code, unsafe_allow_html=True)
