import streamlit as st # streamlit은 st로 줄여서 쓴다.
import time
import datetime
import pandas as pd
import folium

# 페이지 선택기
page = st.sidebar.selectbox("Choose a page", ["Page 1", "Page 2"])

if page == "Page 1":
    st.title("Page 1")
    st.write("This is the content of Page 1")
    # 여기에 페이지 1의 내용을 추가합니다.
    # 예를 들어, 데이터 로드 및 시각화 등을 추가할 수 있습니다.
        # 데이터프레임
    map_data = pd.DataFrame({
        'LATITUDE': [37.5666791, 35.1799528, 35.8713, 37.456, 35.1594647, 36.3497007, 35.5391697, 36.4799999, 37.2884675, 37.8810569, 36.6357, 36.6593, 35.8168271, 34.8159, 35.8583887, 35.2013118, 33.4998289],
        'LONGITUDE': [126.9782914, 129.0752365, 128.6018, 126.7052, 126.8515034, 127.3849016, 129.3119136, 127.289, 127.0535231, 127.7297641, 127.4915, 126.6729, 127.1471024, 126.4629, 128.59277490705324, 128.22473746261176, 126.5313902],
        'City': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '춘천', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
        'Values': [350, 120, 15, 195, 130, 200, 85, 120, 115, 150, 120, 115, 150, 120, 115, 140, 110]
    })

    # 남한의 대략적인 중앙 위치 (위도, 경도)
    south_korea_center = [36.5, 127.5]

    # 지도 객체 생성 (남한의 중앙으로 설정)
    my_map = folium.Map(
        location=south_korea_center,  # 남한 중앙 위도와 경도
        zoom_start=7  # 확대 수준을 적절히 조정
    )

    # 지도 커스텀
    # 지도에 원형 마커와 값 추가
    for index, row in map_data.iterrows():  # 데이터프레임 한 행 씩 처리
        folium.CircleMarker(
            location=[row['LATITUDE'], row['LONGITUDE']],  # 원 중심- 위도, 경도
            radius=row['Values'] / 20,  # 원의 반지름
            color='red',  # 원의 테두리 색상
            fill=True,  # 원을 채움
            fill_opacity=0.6  # 원의 내부를 채울 때의 투명도 (0.6으로 조정)
        ).add_to(my_map)

        folium.Marker(
            location=[row['LATITUDE'], row['LONGITUDE']],  # 값 표시 위치- 위도, 경도
            icon=folium.DivIcon(
                html=f"""
                <div style="
                    font-size: 14pt; 
                    color: black; 
                    font-weight: bold; 
                    text-align: center;
                    white-space: nowrap;
                ">
                    {row['City']}<br>{row['Values']}
                </div>
                """
            ),  # 값 표시 방식
        ).add_to(my_map)

    # 지도 제목과 캡션 추가
    st.title('지도로 볼 수 있는 데이터')

    # 지도 시각화
    st.components.v1.html(my_map._repr_html_(), width=800, height=600)

elif page == "Page 2":
    st.title("Page 2")
    st.write("This is the content of Page 2")
    # 여기에 페이지 2의 내용을 추가합니다.
    # 예를 들어, FAQ 내용이나 다른 정보를 추가할 수 있습니다.



