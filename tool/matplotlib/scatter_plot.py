import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')

np.random.seed(19680801)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.scatter(x, y, 
           c=colors,       # 顏色數組
           s=sizes,        # 大小數組
           alpha=0.5,      # 透明度
           cmap='viridis') # 顏色映射

# 顯示顏色條
plt.colorbar()

plt.title('隨機散點圖')
plt.xlabel('X值')
plt.ylabel('Y值')
plt.show()
