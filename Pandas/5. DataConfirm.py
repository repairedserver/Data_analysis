import pandas as pd
df = pd.read_csv('people.csv', index_col='이름')
print(df)

print(df.describe())
print(df.info())
# print(df.head()) # 처음 5개의 row를 가져옴
print(df.head(6)) # 처음 6개의 row를 가져옴
print(df.tail()) # 마지막 5개의 row를 가져옴

print(df['키'].max())
print(df['키'].nlargest(4)) # 키 큰 사람 순서대로 4명 출력