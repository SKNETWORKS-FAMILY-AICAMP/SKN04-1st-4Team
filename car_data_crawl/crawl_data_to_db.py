import pandas as pd 
import psycopg2

data = pd.read_csv('./merged_file.csv').rename(columns={'Unnamed: 0':'지역'})


## region table 
# 데이터베이스에 연결
try:
    with psycopg2.connect(
        host='192.168.0.87',
        dbname='postgres',
        user='postgres',
        password='qksrkqek12',
        port=8874
    ) as conn:
        with conn.cursor() as cur:
            # region 테이블에 지역 값을 삽입하는 쿼리 구성
            insert_query = """
                INSERT INTO project1.region (region_id, region_name)
                VALUES (%s, %s)
            """
            
            # 데이터프레임의 컬럼에 데이터 넣기 
            for r_id, region in enumerate(data['지역'].loc[1:]):
                # 예를 들어 현재 연도를 함께 삽입하려는 경우
                cur.execute(insert_query, (r_id, region))
            
            # 변경사항 커밋
            conn.commit()
            print("All regions have been inserted successfully.")

except psycopg2.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")



## year table
# 데이터베이스에 연결
try:
    with psycopg2.connect(
        host='192.168.0.87',
        dbname='postgres',
        user='postgres',
        password='qksrkqek12',
        port=8874
    ) as conn:
        with conn.cursor() as cur:
            # year 테이블에 지역 값을 삽입하는 쿼리 구성
            insert_query = """
                INSERT INTO project1.year (year_id, year_value)
                VALUES (%s, %s)
            """
            
            # 데이터프레임의 '지역' 컬럼을 순차적으로 year 테이블에 삽입
            for y_id, year_val in enumerate(list(data.columns)[1:]):
                # 예를 들어 현재 연도를 함께 삽입하려는 경우
                cur.execute(insert_query, (y_id, year_val))
            
            # 변경사항 커밋
            conn.commit()
            print("All regions have been inserted successfully.")

except psycopg2.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")


# registrations table
wo_total = data.drop(index=0)

# 데이터베이스에 연결
try:
    with psycopg2.connect(
        host='192.168.0.87',
        dbname='postgres',
        user='postgres',
        password='qksrkqek12',
        port=8874
    ) as conn:
        with conn.cursor() as cur:
            # registration 테이블에 지역 값을 삽입하는 쿼리 구성
            insert_query = """
                INSERT INTO project1.registrations (registration_id, region_id, year_id, registration_val)
                VALUES (%s, %s, %s, %s)
            """
            registration_id = 0
            # 데이터프레임의 '지역' 컬럼을 순차적으로 year 테이블에 삽입
            for region_id, (region_name, row) in enumerate(wo_total.iterrows()):
                for y_id, year_val in enumerate(list(wo_total.columns[1:])):
                    registration_val = row[year_val]
                    cur.execute(insert_query, (registration_id, region_id, y_id, registration_val))
                    registration_id += 1
            
            # 변경사항 커밋
            conn.commit()
            print("All regions have been inserted successfully.")

except psycopg2.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")



# total_sum table
total_df = data.loc[0]
# 데이터베이스에 연결
try:
    with psycopg2.connect(
        host='192.168.0.87',
        dbname='postgres',
        user='postgres',
        password='qksrkqek12',
        port=8874
    ) as conn:
        with conn.cursor() as cur:
            # registration 테이블에 지역 값을 삽입하는 쿼리 구성
            insert_query = """
                INSERT INTO project1.total_sum (sum_id, year_id, total_registration)
                VALUES (%s, %s, %s)
            """
            sum_id = 0
            # 데이터프레임의 '지역' 컬럼을 순차적으로 year 테이블에 삽입
            for y_id, regi_val in enumerate(total_df[1:]):
                cur.execute(insert_query, (sum_id, y_id, int(regi_val)))
                sum_id += 1
            
            # 변경사항 커밋
            conn.commit()
            print("All regions have been inserted successfully.")

except psycopg2.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")



