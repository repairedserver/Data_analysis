import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

def custom_autopct(pct):
    return '{:.0f}%'.format(pct) if pct >= 10 else ''

values = [30, 25, 6, 10, 22, 40]
labels = ['C', 'Python', 'C#', 'JAVA', 'C++', 'ECT']
# colors = ['r', 'g', 'b', 'y', 'm', 'c']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff',]
explode = [0.05] * 6
plt.pie(values, labels=labels, autopct='%.1f', colors=colors, explode=explode)
plt.show()
wedgeprops = {'width': 0.25, 'edgecolor': 'w', 'linewidth': 3}
plt.pie(values, labels=labels, autopct=custom_autopct, colors=colors, explode=explode, wedgeprops=wedgeprops)
plt.show()
