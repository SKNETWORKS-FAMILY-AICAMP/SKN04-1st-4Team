import numpy as np
import pandas as pd
import glob

# 파일 읽기 
prev_data_path = glob.glob('./125704*.xlsx')
prev_data_df = pd.read_excel(prev_data_path[0])[:-2] # 뒤에 필요 없는 부분은 제거 

# 나중에 인덱스로 사용할 합계, 지역명들은 따로 저장 
index_values = prev_data_df['통계표명:'].iloc[2:].values 

# 연도에 대한 값들을 column으로 
prev_data_df.columns = prev_data_df.iloc[1]
prev_data_df = prev_data_df.drop(index=[0, 1])

# 지역을 인덱스로 
prev_data_df.index = index_values
prev_data_df = prev_data_df.drop(prev_data_df.columns[0], axis=1)


latest_data_path = glob.glob('./*_시도별_*.xlsx')
latest_data_df = pd.read_excel(latest_data_path[0])

# 나중에 인덱스로 사용할 합계, 지역명들은 따로 저장 
index_values = latest_data_df['시도명(1)'].iloc[2:].values 

# 지역을 인덱스로 
latest_data_df = latest_data_df.drop(index=[0, 1])
latest_data_df.index = index_values
latest_data_df = latest_data_df.drop(latest_data_df.columns[[0,1]], axis=1)


# 달 별 총 합이 아니라 해당 연도 12월 데이터로 하면 됨 
# columns_to_sum_2023 = latest_data_df.iloc[:, :12]
# sum_by_region = columns_to_sum_2023.sum(axis=1)
# total_sum = sum(sum_by_region)
# total_sum

# 2023, 2024 데이터 붙이기 
total_df = pd.concat([prev_data_df, latest_data_df['2023.12']], axis=1)
total_df = pd.concat([total_df, latest_data_df['2024.07']], axis=1)

# column명 기존 형식이랑 통일 
total_df = total_df.rename(columns={'2023.12':'2023', '2024.07':'2024'})
total_df.loc['합계'] = total_df.loc['합계'].str.replace(',', '')

# 합계 값 채워넣기
total_df.loc['합계', '2023'] = total_df['2023'].sum()
total_df.loc['합계', '2024'] = total_df['2024'].sum()

# 기존에 숫자 넣는 방식이랑 같은 형식으로
total_df['2023'] = (total_df['2023'] / 10000).round().astype(int)
total_df['2024'] = (total_df['2024'] / 10000).round().astype(int)

# 전체 값들 int로 변환
total_df = total_df.astype(int)

total_df.to_csv('./merged_file.csv')