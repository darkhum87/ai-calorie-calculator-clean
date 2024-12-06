import os
import openai
import streamlit as st

# OpenAI API Key를 환경 변수에서 가져옵니다
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("OpenAI API Key가 설정되지 않았습니다. 환경 변수를 확인하세요.")
else:
    openai.api_key = openai_api_key

st.title("AI Calorie Calculator")
st.write("음식 사진을 업로드하면 칼로리를 예측합니다.")

uploaded_file = st.file_uploader("음식 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)
    st.write("이미지를 분석 중입니다...")

    # OpenAI API 호출 (예: 이미지 분석)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Describe the food in this image and estimate its calorie content.",
        max_tokens=100,
    )
    st.write("결과:", response["choices"][0]["text"])
