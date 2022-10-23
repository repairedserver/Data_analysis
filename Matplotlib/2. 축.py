import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.xlabel('X축', color='red', loc='right')
plt.ylabel('Y축', color='blue', loc='top')
plt.title('꺾은선 그래프', fontdict={'size' : 20})
plt.show()

