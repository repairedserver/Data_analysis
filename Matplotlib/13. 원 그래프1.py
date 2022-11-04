import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

values = [30, 25, 6, 10, 22, 40]
# values = [1, 1, 1, 1, 1, 1]
labels = ['C', 'Python', 'C#', 'JAVA', 'C++', 'ECT']
# plt.pie(values, labels=labels, autopct='%.1f', startangle=90, counterclock=False)
# plt.show()

# explode = [0.2, 0.1, 0, 0, 0, 0]
explode = [0.05] * 6
plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1, 0.3))
plt.show()