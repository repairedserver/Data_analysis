import pandas as pd
import numpy as np
df = pd.read_csv('people.csv')

print(df.fillna('없음')) #빈칸을 없음 이라고 채움

df['학교'] = np.nan # 학교 데이터 전체를 NaN으로 만듬
print(df)

<<<<<<< HEAD
print(df.dropna()) # 전체 데이터 중 NaN을 포함하는 데이터 삭제
print(df.dropna(axis='index', how='any')) #NaN이 하나라도 있는 row 삭제

print(df.dropna(axis='columns', how='all')) # 전체 데이터가 NaN인 경우에만 column 삭제
=======
print(df.dropna()) # 전체 데이터 중 NaN을 포함하는 데이터 삭제
>>>>>>> main
