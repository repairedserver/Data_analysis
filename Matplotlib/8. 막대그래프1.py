import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

labels = ["김하재", "유현세", "이담현"]
values = [190, 187, 210]
colors = ['r', 'g', 'b']
plt.bar(labels, values, color=colors)
plt.show()

labels = ["김하재", "유현세", "이담현"]
values = [190, 187, 210]
plt.bar(labels, values, width=0.5)
plt.ylim(150, 220)
plt.show()

labels = ["김하재", "유현세", "이담현"]
values = [190, 187, 210]
plt.bar(labels, values, width=0.5)
plt.xticks(rotation=45)
plt.show()