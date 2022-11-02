import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('score.csv')
<<<<<<< HEAD
plt.plot(df['이름'], df['수학'])
plt.plot(df['이름'], df['영어'])
plt.grid(axis='y', color='red')
plt.show()
=======
plt.plot(df['이름'], df['키'])
>>>>>>> main
