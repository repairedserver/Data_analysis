import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')
plt.bar(df['이름'], df['국어'])
plt.bar(df['이름'], df['영어'], bottom=df['국어'])
plt.bar(df['이름'], df['수학'], bottom=df['국어']+df['영어'])
plt.xticks(rotation=60)
plt.legend()
plt.show()