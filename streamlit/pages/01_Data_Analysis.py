import streamlit as st # streamlit은 st로 줄여서 쓴다.
import time
import datetime
import pandas as pd
import folium

import psycopg2
import plotly.express as px
import random
import plotly.graph_objects as go

# 페이지 선택기
page = st.sidebar.selectbox("Choose a page", ["막대그래프", "지도"])

if page == "막대그래프": 
    def fetch_total_sum_data():
        try:
            # PostgreSQL 데이터베이스에 연결
            conn = psycopg2.connect(
                host='192.168.0.87',
                dbname='postgres',
                user='postgres',
                password='qksrkqek12',
                port=8874
            )

            # SQL 쿼리 실행
            query = """
            SELECT ts.year_id, y.year_value, ts.total_registration
            FROM project1.total_sum ts 
            JOIN project1.year y ON ts.year_id = y.year_id
            ORDER BY ts.year_id
            """
            df = pd.read_sql(query, conn)
            
            return df

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            if conn:
                conn.close()
                


    def fetch_region_year_data(region_name):
        try:
            # PostgreSQL 데이터베이스에 연결
            conn = psycopg2.connect(
                host='192.168.0.87',
                dbname='postgres',
                user='postgres',
                password='qksrkqek12',
                port=8874
            )

            # SQL 쿼리 실행
            query = """
            SELECT y.year_value, SUM(CAST(rg.registration_val AS NUMERIC)) AS total_registration
            FROM project1.registrations rg
            JOIN project1.year y ON rg.year_id = y.year_id
            JOIN project1.region r ON rg.region_id = r.region_id
            WHERE r.region_name = %s
            GROUP BY y.year_value
            ORDER BY y.year_value
            """
            df = pd.read_sql(query, conn, params=(region_name,))
            
            return df

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            if conn:
                conn.close()


############################################################################################################
# PostgreSQL에서 연도별 총 합 가져오기 
    total_sum_df = fetch_total_sum_data()
    st.title("연도별 전국 자동차 등록 현황 ")
    # 데이터가 정상적으로 가져와졌는지 확인
    if total_sum_df is not None:
        
        whole_data = total_sum_df['total_registration']
        
        # 회사 지분을 나타내는 임의의 데이터
        custom_data = [int(y_val * (random.uniform(0.1, 0.3))) for y_val in whole_data]

        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x = total_sum_df['year_value'],
            y = whole_data,
            name = '총 등록 대수',
            marker_color = 'lightblue'
        ))
        
        fig.add_trace(go.Bar(
            x = total_sum_df['year_value'],
            y = custom_data,
            name = '엔코 차 등록 수',
            marker_color = 'lightpink'
        ))
        
        fig.update_xaxes(tickmode='linear', dtick=1)
        fig.update_layout(
            barmode='overlay', 
            title="연도별 전국 자동차 등록 대수와 엔코사 자동차 등록 대수 비교",
            xaxis_title="연도",
            yaxis_title="합계(단위: 만대)",
            legend_title="데이터 종류"
        )

        # Streamlit에서 차트 표시
        st.plotly_chart(fig)


    else:
        st.error("Failed to load data from the database.")

    ############################################################################################################

    # Streamlit 앱 시작
    st.title("지역별 연도별 자동차 등록 현황 검색")

    # 사용자 입력 (검색 키워드)
    keyword = st.text_input("연도별 등록 현황을 알고 싶은 지역 이름을 입력하세요:", "")

    # 검색 가능한 지역 목록
    valid_regions = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기",
                    "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]


    if keyword in valid_regions:
        # 데이터베이스에서 해당 지역의 데이터를 가져오기
        region_year_df = fetch_region_year_data(keyword)

        if region_year_df is not None and not region_year_df.empty:
            # Plotly를 사용한 그래프 생성
            fig = px.bar(region_year_df, x='year_value', y='total_registration', 
                        labels={'year_value': '연도', 'total_registration': '합계(단위: 만대)'},
                        title=f"{keyword} 지역의 연도별 자동차 등록 현황",
                        color_discrete_sequence=['#1f77b4'])
            fig.update_xaxes(tickmode='linear', dtick=1)

            # Streamlit에서 차트 표시
            st.plotly_chart(fig)
        else:
            st.warning(f"{keyword} 지역에 대한 데이터를 찾을 수 없습니다.")
    else:
        if keyword:
            st.error("검색 가능한 지역이 아닙니다. 올바른 지역 이름을 입력하세요.")


####
def fetch_registration_by_year(input_year):
    try:
        # PostgreSQL 데이터베이스에 연결
        conn = psycopg2.connect(
            host='192.168.0.87',
            dbname='postgres',
            user='postgres',
            password='qksrkqek12',
            port=8874
        )

        # SQL 쿼리 실행
        query = """
        SELECT r.region_name, reg.registration_val
        FROM project1.registrations reg
        JOIN project1.year y ON reg.year_id = y.year_id
        JOIN project1.region r ON reg.region_id = r.region_id
        WHERE y.year_value = %s;
        """
        df = pd.read_sql(query, conn, params=(input_year,))

        return df

    except psycopg2.Error as e:
        st.error(f"Database error: {e}")
        return None

    finally:
        if conn:
            conn.close()

if page == "지도":
    st.title("연도별 전국 자동차 현황")

    # 연도 입력 받기
    year = st.text_input("연도를 입력해주세요 (예: 2023):", "")

    if year:
        # 연도별 데이터 가져오기
        df = fetch_registration_by_year(year)

        if df is not None and not df.empty:
            # 지도 데이터프레임 생성
            map_data = pd.DataFrame({
                'LATITUDE': [37.5666791, 35.1799528, 35.8713, 37.456, 35.1594647, 36.3497007, 35.5391697, 36.4799999, 37.2884675, 37.8810569, 36.6357, 36.6593, 35.8168271, 34.8159, 35.8583887, 35.2013118, 33.4998289],
                'LONGITUDE': [126.9782914, 129.0752365, 128.6018, 126.7052, 126.8515034, 127.3849016, 129.3119136, 127.289, 127.0535231, 127.7297641, 127.4915, 126.6729, 127.1471024, 126.4629, 128.59277490705324, 128.22473746261176, 126.5313902],
                'City': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '춘천', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
                'Values': df['registration_val']  # 기본 값은 0으로 설정
            })

            # 남한의 대략적인 중앙 위치 (위도, 경도)
            south_korea_center = [36.5, 127.5]

            # 지도 객체 생성 (남한의 중앙으로 설정)
            my_map = folium.Map(
                location=south_korea_center,  # 남한 중앙 위도와 경도
                zoom_start=8  # 확대 수준을 적절히 조정
            )

            # 지도 커스텀
            # 지도에 원형 마커와 값 추가
            for index, row in map_data.iterrows():  # 데이터프레임 한 행 씩 처리
                folium.CircleMarker(
                    location=[row['LATITUDE'], row['LONGITUDE']],  # 원 중심- 위도, 경도
                    radius=int(row['Values']) / 30,  # 원의 반지름
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
            st.title(f'{year}년 데이터')

            # 지도 시각화
            with st.empty():
                st.components.v1.html(my_map._repr_html_(), width=1000, height=600)

        else:
            st.warning(f"{year} 년도에 대한 데이터가 없습니다.")
    else:
        st.info("연도를 입력해주세요.")