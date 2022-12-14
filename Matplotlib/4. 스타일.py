import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]
# plt.plot(x, y, linewidth=5)
# plt.show()

# plt.plot(x, y, marker='o')
# plt.show()

# plt.plot(x, y, marker='o', linestyle='None')
# plt.show()

# plt.plot(x, y, marker='v', markersize=10)
# plt.show()

# plt.plot(x, y, marker='o', markersize=15, markeredgecolor='red', markerfacecolor='yellow')
# plt.show()

# 선 스타일
# plt.plot(x, y, linestyle='--')
# plt.show()

# plt.plot(x, y, linestyle='-.')
# plt.show()

# 선 색
# plt.plot(x, y, color='pink')
# plt.show()

# plt.plot(x, y, color='#ff0000')
# plt.show()

# 포맷
plt.plot(x, y, 'rv-.')
plt.show()

plt.plot(x, y, 'go')
plt.show()

# 축약어
plt.plot(x, y, marker='o', mfc='red', ms=10, mec='b', ls='-.')
plt.show()