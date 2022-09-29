import pandas as pd
df = pd.read_csv('people.csv')

print(df['학교'].replace({'대마':'대마고', '부마':'부마고'}, inplace=True)) # 대마라는 이름의 학교를 대마고로 변경
print(df)

df['학교'] = df['학교'] + '등학교' # 학교에 등학교 단어를 붙임
print(df)