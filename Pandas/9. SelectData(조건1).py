import pandas as pd
df = pd.read_csv('people.csv')

print(df['키'] >= 180) #키가 180 이상인지 True, False 여

tall = (df['키'] >= 175)
print(df[tall])
# print(df[-tall]) # tall을 역으로 적용

print(df.loc[df['키'] >= 180, '수학']) # 키가 180이상인 학생들의 수학 데이터
print(df.loc[df['키'] >= 180, ['이름', '수학', '영어']]) # 키가 180이상인 학생들의 이름, 수학, 영어 데이터

print(df.loc[(df['키'] >= 180) & (df['학교'] == '대마')]) # 키가 180이상인 대마고 학생들
print(df.loc[(df['키'] >= 180) | (df['키'] <= 170)]) # 키가 180이상이거나 170이하인 학생