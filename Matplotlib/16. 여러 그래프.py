import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
plt.suptitle('여러 그래프')
axs[0, 0].bar(df['이름'], df['국어'], label='국어점수')
axs[0, 0].set_title('첫 번째 그래프')
axs[0, 0].legend()
axs[0, 0].set(xlabel='이름', ylabel='점수')
axs[0, 0].set_facecolor('lightyellow')
axs[0, 0].grid(linestyle='--', linewidth=0.5)

axs[0, 1].bar(df['이름'], df['수학'], label='수학점수')
axs[0, 1].set_title('두 번째 그래프')
axs[0, 1].legend()
axs[0, 1].set(xlabel='이름', ylabel='점수')
axs[0, 1].set_facecolor('lightyellow')
axs[0, 1].grid(linestyle='--', linewidth=0.5)

axs[1, 0].bar(df['이름'], df['영어'], label='영어점수')
axs[1, 0].set_title('세 번째 그래프')
axs[1, 0].legend()
axs[1, 0].set(xlabel='이름', ylabel='점수')
axs[1, 0].set_facecolor('lightyellow')
axs[1, 0].grid(linestyle='--', linewidth=0.5)

axs[1, 1].bar(df['이름'], df['사회'], label='사회점수')
axs[1, 1].set_title('네 번째 그래프')
axs[1, 1].legend()
axs[1, 1].set(xlabel='이름', ylabel='점수')
axs[1, 1].set_facecolor('lightyellow')
axs[1, 1].grid(linestyle='--', linewidth=0.5)
plt.show()