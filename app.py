import streamlit as st
import base64
import os

# 1. 페이지 기본 설정 (가장 먼저 와야 함)
st.set_page_config(
    page_title="방문자 리뷰 EVENT!!",
    page_icon="🎁",
    layout="centered"
)

# 2. QR 코드 이미지 처리
# GitHub에 함께 올린 QR 이미지 파일 이름
QR_IMAGE_PATH = "KakaoTalk_20260311_133707826.png"

def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

qr_base64 = get_image_base64(QR_IMAGE_PATH)

# 이미지가 정상적으로 읽히면 해당 이미지를, 없으면 임시 이미지를 보여줍니다.
if qr_base64:
    img_src = f"data:image/png;base64,{qr_base64}"
else:
    # 깃허브에 이미지를 아직 안 올렸을 때 에러 방지용 임시 QR코드
    img_src = "https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=example"

# 3. 화면 디자인 (HTML & CSS)
# 파이썬 f-string 안에서 CSS를 쓸 때는 중괄호를 {{ }} 처럼 두 번 써야 합니다.
html_content = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

    /* Streamlit 기본 UI(헤더, 푸터, 여백) 숨기기 */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .block-container {{padding-top: 2rem; padding-bottom: 0rem; max-width: 600px;}}

    .event-card {{
        font-family: 'Noto Sans KR', sans-serif;
        width: 100%;
        background: linear-gradient(145deg, #1f1f1f 0%, #121212 100%);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
        border: 2px solid #c5a059;
        padding: 40px 30px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-sizing: border-box;
    }}

    .event-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        height: 4px;
        background: #c5a059;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    }}

    .title {{
        color: #c5a059;
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: -1px;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }}

    .subtitle {{
        color: #e5e5e5;
        font-size: 1.15rem;
        font-weight: 500;
        line-height: 1.5;
        margin-bottom: 30px;
    }}

    .highlight {{
        color: #c5a059;
        font-weight: 700;
        font-size: 1.3rem;
    }}

    .qr-wrapper {{
        background-color: #ffffff;
        padding: 15px;
        border-radius: 16px;
        display: inline-block;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        border: 4px solid #333;
    }}

    .qr-wrapper img {{
        width: 180px;
        height: 180px;
        object-fit: contain;
        display: block;
    }}

    .qr-hint {{
        color: #888;
        font-size: 0.85rem;
        margin-top: 8px;
        font-weight: 500;
    }}

    .steps-container {{
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(197, 160, 89, 0.2);
        border-radius: 16px;
        padding: 25px 20px;
        margin-bottom: 30px;
        text-align: left;
    }}

    .step-item {{
        display: flex;
        align-items: center;
        margin-bottom: 16px;
        color: #d1d1d1;
        font-size: 1.05rem;
        font-weight: 500;
    }}

    .step-item:last-child {{
        margin-bottom: 0;
    }}

    .step-number {{
        background-color: #c5a059;
        color: #121212;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 900;
        font-size: 0.95rem;
        margin-right: 12px;
        flex-shrink: 0;
    }}

    .reward-box {{
        background: linear-gradient(90deg, #b38c45, #d4b572, #b38c45);
        color: #111;
        padding: 18px 10px;
        border-radius: 12px;
        font-weight: 900;
        font-size: 1.35rem;
        letter-spacing: -0.5px;
        box-shadow: 0 4px 15px rgba(197, 160, 89, 0.3);
    }}
</style>

<div class="event-card">
    <div class="title">방문자 리뷰 EVENT!!</div>
    
    <div class="subtitle">
        플레이스 저장하고 리뷰 남겨주시면<br>
        <span class="highlight">100% 서비스 당첨!</span>
    </div>

    <div class="qr-wrapper">
        <img src="{img_src}" alt="QR Code">
        <div class="qr-hint">스마트폰 카메라로 스캔해주세요!</div>
    </div>

    <div class="steps-container">
        <div class="step-item">
            <div class="step-number">1</div>
            <div>QR코드 스캔</div>
        </div>
        <div class="step-item">
            <div class="step-number">2</div>
            <div>네이버 플레이스 <strong>'저장'</strong> 클릭</div>
        </div>
        <div class="step-item">
            <div class="step-number">3</div>
            <div>정성스러운 <strong>방문자 리뷰</strong> 작성</div>
        </div>
        <div class="step-item">
            <div class="step-number">4</div>
            <div>직원에게 <strong>리뷰 화면</strong> 보여주세요</div>
        </div>
    </div>

    <div class="reward-box">
        서비스 / 음료 / 할인 100% 제공
    </div>
</div>
"""

# 4. Streamlit에 HTML 렌더링하기
st.markdown(html_content, unsafe_allow_html=True)