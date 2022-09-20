import pandas as pd
# 2. DataFrame
# 2차원 데이터 (Series들의 모음)
data = {
    '이름' : ['김', '이', '최', '문', '유', '강'],
    '학교' : ['대마', '대마', '부마', '부마', '대마', '대마'],
    '키' : [197, 184, 168, 187, 188, 202],
    '국어' : [90, 40, 80, 40, 15, 80],
    '영어' : [85, 35, 75, 60, 20, 100],
    '수학' : [100, 50, 70, 70, 10, 95],
    '과학' : [95, 55, 80, 75, 35, 85],
    '사회' : [85, 25, 75, 80, 10, 80]
}
print(data['이름'])
print(data['학교'])

df = pd.DataFrame(data)
print(df)
# print(df['이름'])
print(df[['이름', '학교', '키']])

# DataFrame 객체 생성
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
print(df)

# DataFrame 객체 생성 (column 지정)
df = pd.DataFrame(data, columns=['학교', '이름', '키'])
print(df)