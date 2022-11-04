import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

values = [30, 25, 6, 10, 22, 40]
labels = ['C', 'Python', 'C#', 'JAVA', 'C++', 'ECT']
plt.pie(values, labels=labels, autopct='%.1f', startangle=90, counterclock=False)
