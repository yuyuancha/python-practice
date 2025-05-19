import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')
print(plt.style.available)  # 查看可用樣式
plt.style.use('dark_background')     # 套用樣式

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(0, 10, 100)
y = np.sin(x)

categories = ['蘋果', '香蕉', '橙子', '西瓜']
sales = [45, 32, 28, 51]

labels = ['台北', '台中', '高雄', '花蓮']
sizes = [45, 30, 15, 10]

# 子圖1: 折線圖
axs[0,0].plot(x, y, 'r-')
axs[0,0].set_title('折線圖')

# 子圖2: 柱狀圖
axs[0,1].bar(categories, sales)
axs[0,1].set_title('柱狀圖')

# 子圖3: 散點圖
axs[1,0].scatter(x, y)
axs[1,0].set_title('散點圖')

# 子圖4: 圓餅圖
axs[1,1].pie(sizes, labels=labels)
axs[1,1].set_title('圓餅圖')

plt.tight_layout()
plt.show()
