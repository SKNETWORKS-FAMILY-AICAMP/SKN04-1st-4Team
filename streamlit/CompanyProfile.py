import streamlit as st # streamlit은 st로 줄여서 쓴다.
import time
import datetime

# 이미지 파일 경로 설정
image_path = "C:\\Users\\Playdata\\Documents\\git\\Project_4\\SKN04-1st-4Team\\logo.png"  # 이미지 파일의 경로

# 이미지 표시
st.image(image_path ,use_column_width=True)

st.title('회사소개')
st.text("열심히 자동차를 만들고 전국 자동차 수를 파악하는 기업")


col1, col2= st.columns([0.3, 0.7])

with col1:
    st.header('이름')
    st.subheader('오정연')
    st.subheader('김현재')
    st.subheader('권오셈')
    st.subheader('오종수')

with col2:
    st.header('역할')
    st.subheader('팀장 : 데이터 크롤링, DB')
    st.subheader('팀원 : 데이터 크롤링, ㄴㄴㄴㄴ')
    st.subheader('팀원 : 데이터 크롤링, ㄴㄴㄴㄴ')
    st.subheader('팀원 : 데이터 크롤링, ㄴㄴㄴㄴ')

