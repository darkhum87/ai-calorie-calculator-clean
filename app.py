import os
import openai
import streamlit as st
from PIL import Image

# OpenAI API 키를 Streamlit Secrets에서 가져옵니다.
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit 앱 제목
st.title("AI Calorie Calculator")
st.write("음식 사진을 업로드하면 칼로리를 예측합니다.")
st.write("음식 사진을 업로드하세요")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 업로드된 이미지를 표시
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # OpenAI API를 사용하여 분석 요청
    st.write("이미지 분석 중입니다. 잠시만 기다려 주세요...")

    try:
        # 업로드된 파일을 OpenAI API에서 처리할 수 있도록 파일 객체로 전달
        uploaded_file.seek(0)  # 파일 포인터를 시작으로 재설정
        response = openai.Image.create(
            file=uploaded_file,
            purpose="calorie_estimation"
        )
        # 샘플 응답 처리
        calories = response.get("calories", "N/A")
        st.success(f"예상 칼로리: {calories} kcal")
    except Exception as e:
        st.error(f"예상 칼로리 계산 중 오류 발생: {e}")
else:
    st.info("이미지를 업로드하세요.")
