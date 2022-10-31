import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]

#백신접종인구
days = [1, 2, 3]
az = [2, 6, 10]
pfizer = [5, 1, 3]
moderna = [1, 2, 5]

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o')
plt.plot(days, moderna, label='moderna', marker='s')
plt.legend(ncol=3)
plt.show()