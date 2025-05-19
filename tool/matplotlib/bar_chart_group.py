import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')
labels = ['Q1', 'Q2', 'Q3', 'Q4']
men_means = [20, 35, 30, 35]
women_means = [25, 32, 34, 20]

x = np.arange(len(labels))
width = 0.35  # 柱體寬度

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='男性')
rects2 = ax.bar(x + width/2, women_means, width, label='女性')

ax.set_ylabel('銷售額')
ax.set_title('季度銷售性別比較')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# 在柱體上顯示數值
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

plt.show()
