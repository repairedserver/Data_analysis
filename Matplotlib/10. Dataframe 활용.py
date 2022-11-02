import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')
plt.plot(df['이름'], df['수학'])
plt.plot(df['이름'], df['영어'])
plt.grid(axis='y', color='red', alpha=0.3, linestyle='--', linewidth=1)
plt.show()