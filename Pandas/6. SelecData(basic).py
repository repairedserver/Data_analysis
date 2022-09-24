import pandas as pd
df = pd.read_csv('people.csv' )
print(df)

# Column 선택
print(df['이름'])

print(df[df.columns[-1]])

print(df['영어'][0:5]) # 0에서 4까지의 데이터 가져옴

print(df[['이름', '키']][0:4])