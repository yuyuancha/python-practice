import torch
import torch.nn.functional as F

# 輸入資料
data = [
    [1, 2, 0, 3, 1],
    [0, 1, 2, 3, 1],
    [1, 2, 1, 0, 0],
    [5, 2, 3, 1, 1],
    [2, 1, 0, 1, 1]
]

# 卷積核
core = [
    [1, 2, 1],
    [0, 1, 0],
    [2, 1, 0]
]

# 將資料轉換為張量
input = torch.tensor(data)
kernel = torch.tensor(core)

# 重新調整大小
input = torch.reshape(input, (1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))

# 輸出 stride=1 的卷積結果
output = F.conv2d(input, kernel, stride=1)
print(output)

# 輸出 stride=2 的卷積結果
output2 = F.conv2d(input, kernel, stride=2)
print(output2)

# 輸出 stride=1, padding=1 的卷積結果
output3 = F.conv2d(input, kernel, stride=1, padding=1)
print(output3)
