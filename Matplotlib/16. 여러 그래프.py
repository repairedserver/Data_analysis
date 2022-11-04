import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.subtitle('여러 그래프')
axs[0, 0].bar(df['이름'], df['국어'], label='국어점수')
axs[0, 0].set_title('첫 번째 그래프')
axs[0, 0].legend()
axs[0, 0].set(xlabel='이름', ylabel='점수')