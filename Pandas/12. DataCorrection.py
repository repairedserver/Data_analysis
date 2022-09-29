import pandas as pd
df = pd.read_csv('people.csv')

print(df['학교'].replace({'대마':'대마고', '부마':'부마고'}, inplace=True)) # 대마라는 이름의 학교를 대마고로 변경
print(df)

df['학교'] = df['학교'] + '등학교' # 학교에 등학교 단어를 붙임
print(df)

# Column 추가
df['총합점수'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']

df['결과'] = 'Fall'
df.loc[df['총합점수'] > 400, '결과'] = 'Pass'

print(df)

# Column 제거
df = df.drop(columns=['총합점수'])
print(df)

# Row 삭제
df = df.drop(index=4) # 4번째 인덱스에 있는 학생 정보 삭제
print(df)

# Row 추가
df.loc[6] = ['조', '대마고등학교', '180', '90', '90', '95', '100', '0', 'Pass']
print(df)

# Cell 수정
df.loc[3, '키'] = '185'
print(df)

# Column 순서 변경
col = list(df.columns)
df = df[[col[-1]] + col[0:-1]] # 맨 뒤에 있는 column을 앞으로 가져오고 전부 뒤로 땡김
print(df)