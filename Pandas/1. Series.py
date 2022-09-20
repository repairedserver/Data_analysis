import pandas as pd
# 1. Series
# 1차원 데이터 (정수, 실수, 문자열 등)
temp = pd.Series([-10, 0, 10, 15])
print(temp)
#print(temp[2])

# 2. Series 객체 생성 (index 지정)
temp = pd.Series([-10, 0, 10, 15], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
print(temp['Jan']) # 인덱스 Jan에 해당하는 데이터 출력