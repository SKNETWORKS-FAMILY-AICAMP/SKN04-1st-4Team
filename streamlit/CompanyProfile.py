import streamlit as st # streamlit은 st로 줄여서 쓴다.
import time
import datetime

# 이미지 파일 경로 설정
image_path = "../logo.png"  # 이미지 파일의 경로

# 이미지 표시
st.image(image_path ,use_column_width=True)

st.markdown("<h1 style='text-align: center;'>엔코아 자동차</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>전국에서 최대 30%의 지분을 차지하는 엔코아 자동차! </h5>", unsafe_allow_html=True)


st.text("")
st.text("")
st.text("")


# 창립멤버 섹션
st.markdown("<h2 style='text-align: center; color: #2B6465;'>창립멤버</h2>", unsafe_allow_html=True)

# 멤버 목록
members = ["오정연", "김현재", "권오셈", "오종수"]

# 창립멤버를 카드 형식으로 표시
for member in members:
    st.markdown(f"""
        <div style='display: flex; justify-content: center; align-items: center; margin-top: 10px;'>
            <div style='background-color: #f9f9f9; padding: 8px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); width: 50%; text-align: center;'>
                <h3 style='margin: 0; color: #333;'>{member}</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

