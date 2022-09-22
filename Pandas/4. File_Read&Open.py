# DataFrame 객체를 excel, csv, txt 파일로 저장 및 열기
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
df.index.name = '번호번호'

#df.to_csv('people.csv', encoding='utf-8-sig')
df.to_csv('people.csv', encoding='utf-8-sig', index=False)

df.to_csv('people.txt', sep='\t') # tab으로 구분된 텍스트

# df1 = pd.read_csv('people.csv', skiprows=[1, 3, 4]) # skiprows : 무시하고 싶은 줄
# df1 = pd.read_csv('people.csv', nrows=4) # nrows : 가져오고 싶은 줄
df1 = pd.read_csv('people.csv', skiprows=2, nrows=4) # 처음 2줄 무시 후 그다음 4줄을 가져옴
print(df1)