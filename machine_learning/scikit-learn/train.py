# 練習 scikit-learn 套件: 訓練模型
# 預期訓練出 y = 10 * x - 12 的模型
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Linear Regression 機器學習模型
from sklearn.linear_model import LinearRegression

# 設定訓練資料
train_x = np.random.rand(100, 1) * 10
train_y = 10 * train_x - 12

model = LinearRegression(
    fit_intercept=True, # 是否考慮到截距來最佳化模型
)

# 5. 使用 model.fit 進行模型訓練
# 模型輸入為 train_x，預測目標為 train_y
model.fit(train_x, train_y)

# 6. 確認模型是否訓練成功
# 此範例中使用 model.score 與視覺化的方式觀察
print(model.score(train_x, train_y))
plt.scatter(
    train_x,
    train_y,
    marker='1'
)
plt.scatter(
    train_x,
    model.predict(train_x),
    marker='2',
    color='red'
)
plt.show()

pickle.dump(model, open('./model.pickle', 'wb'))
