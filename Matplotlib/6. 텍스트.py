import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y, marker='o')

for idx, txt in enumerate(y):
    plt.text(x[idx] - 0.05, y[idx] + 0.3, txt)

plt.show()

