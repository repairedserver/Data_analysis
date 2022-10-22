import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False # 한글폰트 사용시 글자깨짐 방지
x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.title('Line Graph')
plt.show()

plt.plot([-1, 0, 1], [-5, -1, -2])
plt.show()