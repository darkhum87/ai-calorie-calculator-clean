import os
import openai
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

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

    # 이미지를 base64로 인코딩
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # OpenAI API를 사용하여 분석 요청
    st.write("이미지 분석 중입니다. 잠시만 기다려 주세요...")
    try:
        # 이미지 데이터를 base64로 전달
        response = openai.Completion.create(
            model="text-davinci-003",  # 대체 가능한 모델
            prompt=f"이미지를 분석해 칼로리를 추정하세요. 이미지 데이터: {img_base64}",
            max_tokens=100
        )
        # 샘플 응답 처리
        st.success(f"예상 칼로리: {response['choices'][0]['text'].strip()} kcal")
    except Exception as e:
        st.error(f"예상 칼로리 계산 중 오류 발생: {e}")
else:
    st.info("이미지를 업로드하세요.")
