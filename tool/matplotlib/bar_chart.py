import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', family='Heiti TC')

categories = ['蘋果', '香蕉', '橙子', '西瓜']
sales = [45, 32, 28, 51]

plt.bar(categories, sales,
       color='#66b3ff',     # 柱體顏色
       edgecolor='black',   # 邊框顏色
       width=0.6)           # 柱體寬度

# 設定圖表標題
plt.title('水果銷售量比較')

# 設定 y 軸名稱
plt.ylabel('銷售量(公斤)')

# x 軸名稱旋轉角度
plt.xticks(rotation=45)

plt.show()
