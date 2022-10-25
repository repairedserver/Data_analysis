import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y, linewidth=5)
plt.show()

plt.plot(x, y, marker='o')
plt.show()