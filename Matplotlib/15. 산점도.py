import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

sizes = np.random.rand(8) * 1000

df = pd.read_csv('score.csv')
df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3)
plt.figure(figsize=(10, 10))
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()