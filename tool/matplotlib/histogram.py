import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')

data = np.random.normal(170, 10, 250)  # 平均170, 標準差10

plt.hist(data, 
        bins=30,            # 柱體數量
        density=True,       # 顯示概率密度
        color='green',
        alpha=0.7,
        histtype='stepfilled',  # 填充樣式
        edgecolor='black')

plt.title('身高分佈直方圖')
plt.xlabel('身高(cm)')
plt.ylabel('概率密度')
plt.grid(axis='y', alpha=0.3)
plt.show()
