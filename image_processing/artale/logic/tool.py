import os

def create_when_not_existed(dir_path):
    """
    當資料夾不存在時，創建資料夾
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
