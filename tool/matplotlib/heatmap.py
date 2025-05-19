import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')

data = np.random.rand(10, 12)

plt.imshow(data, 
          cmap='hot',      # 顏色映射
          interpolation='nearest')

plt.colorbar()
plt.title('隨機熱力圖')
plt.xticks(range(12))
plt.yticks(range(10))
plt.show()
