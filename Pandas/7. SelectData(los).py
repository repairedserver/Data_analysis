# 이름을 이용해 원하는 row에서 원하는 col 선택
import pandas as pd
df = pd.read_csv('people.csv' )
print(df.loc[0]) # 인덱스 0에 해당하는 전체 데이터
print(df.loc[0, '국어']) # 인덱스 0에 해당하는 국어 데이터
print(df.loc[[0, 1], '영어']) # 인덱스 0과 1에 해당하는 영어 데이터
print(df.loc[0:4, '국어':'영어']) # 인덱스 0부터 4까지 해당하는 국어, 영어 데이터