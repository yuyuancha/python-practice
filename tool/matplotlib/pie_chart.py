import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('font', family='Heiti TC')

labels = ['台北', '台中', '高雄', '花蓮']
sizes = [45, 30, 15, 10]
explode = (0.1, 0, 0, 0)  # 突出顯示第一塊

plt.pie(sizes, 
       explode=explode,
       labels=labels,
       autopct='%1.1f%%',  # 顯示百分比格式
       shadow=True,         # 陰影效果
       startangle=90,       # 起始角度
       colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

plt.axis('equal')  # 正圓形
plt.title('台灣地區銷售佔比')
plt.show()
