import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data,
           vert=True,       # 垂直顯示
           patch_artist=True,  # 填充顏色
           labels=['A組', 'B組', 'C組'],
           boxprops=dict(facecolor='lightblue'))

plt.title('各組數據分佈比較')
plt.ylabel('測量值')
plt.grid(axis='y', alpha=0.3)
plt.show()
