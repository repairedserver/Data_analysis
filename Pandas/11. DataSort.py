import pandas as pd
df = pd.read_csv('people.csv')

print(df.sort_values('키')) # 키 순서대로 오름차순 정렬
print(df.sort_values('키', ascending=False)) # 키 순서대로 내림차순 정렬

print(df.sort_values(['수학', '영어'], ascending=False)) # 수학을 기준으로 내림차순 정렬하되 점수가 똑같으면 영어 순서대로 정렬

print(df['과학'].sort_values(ascending=False)) # 과학만 내림차순 정렬