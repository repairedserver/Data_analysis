import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'AppleGothic'
mat.rcParams['font.size'] = 15
mat.rcParams['axes.unicode_minus'] = False

labels = ["김하재", "유현세", "이담현"]
values = [190, 187, 210]

plt.barh(labels, values)
plt.xlim(180, 220)
barh = plt.barh(labels, values)
barh[0].set_hatch('/')
barh[1].set_hatch('x')
barh[2 ].set_hatch('..')
plt.show()

for idx, rect in enumerate(barh):
    plt.text(idx, rect.get_height(), values[idx])
plt.show()