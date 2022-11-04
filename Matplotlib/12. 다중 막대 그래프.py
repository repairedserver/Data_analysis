import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')
arr = np.arange(5)
N = df.shape[0]
w = 0.25
index = np.arange(N)
plt.bar(index-w, df['국어'])
plt.show()