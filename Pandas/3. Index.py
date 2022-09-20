import pandas as pd
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
df = pd.DataFrame(data)
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
print(df)
print(df.index)

df.index.name = '번호번호'
print(df)

# Index 초기화
#df = df.reset_index(drop=True) # 원래 쓰던 인덱스 '번호번호'를 지움
#print(df)

# 변수 따로 안쓰고 바로 반영하기
df.reset_index(drop=True, inplace=True)
print(df)

# 지정한 column으로 인덱스 설정
df.set_index('이름', inplace=True)
print(df)

# 오름차순 정렬
#df.sort_index(inplace=True)
#print(df)

# 내림차순 정렬
df.sort_index(inplace=True ,ascending=False)
print(df)