import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 設定中文字體
matplotlib.rc('font', family='Heiti TC')

# 利用 numpy 產生 y = sin(x) 資料
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, 
        color='blue',       # 線條顏色
        linestyle='-',      # 實線(-)/虛線(--)/點線(:)
        linewidth=2,        # 線條粗細
        marker='o',         # 數據點標記樣式
        markersize=3,       # 標記大小
        label='sin(x)')     # 圖例標籤

plt.title('正弦函數曲線', fontsize=14)
plt.xlabel('X軸', fontsize=12)
plt.ylabel('Y軸', fontsize=12)

# 顯示網格線
plt.grid(True, alpha=0.3)

# 顯示圖例
plt.legend()

# 自動調整間距
plt.tight_layout()

# 顯示圖表
plt.show()
