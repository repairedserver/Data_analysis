import pandas as pd
df = pd.read_csv('people.csv')

print(df.iloc[0]) # 0번째 위치의 데이터
print(df.iloc[0:5]) # 0에서 5까지 위치의 데이터
print(df.iloc[0, 1]) # 0번째 위치의 1번째 데이터
print(df.iloc[[0, 1], 2]) # 0, 1번째 위치의 2번째 데이터
print(df.iloc[0:2, 0:3]) # 0, 1번째 위치 중 0~2번째 데이터