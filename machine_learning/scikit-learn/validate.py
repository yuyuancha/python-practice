import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.linear_model import LinearRegression

test_x = np.random.rand(15, 1) * 10
test_y = 10 * test_x - 12

# 2. 資料前處理
# 此範例中不需要進行前處理

# 3. 載入訓練過的模型
# 使用 pickle 將儲存於 ./data/model.pickle 的模型讀入
# rb: read in binary mode
model = pickle.load(open('./model.pickle', 'rb'))

# 4. 使用 `model.predict()` 進行預測
# 模型輸入為 test_x，將預測結果保留在 pred_y
pred_y = model.predict(test_x)

# 5. 評估預測結果
# 此範例中使用 model.score 與視覺化的方式觀察
print(model.score(test_x, test_y))
plt.scatter(
    test_x,
    test_y,
    marker='1'
)
plt.scatter(
    test_x,
    pred_y,
    marker='2',
    color='red'
)
plt.show()
