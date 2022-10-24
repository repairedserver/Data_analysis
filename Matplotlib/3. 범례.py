import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y, label='어쩌고 데이터')
plt.legend(loc='upper right')
plt.show()

plt.plot(x, y, label='범례')
plt.legend(loc=(0.5, 0.5))
plt.show()