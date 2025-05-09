import cv2
import numpy as np
import os

def cut_image_and_save(image_path, output_dir, cut_height=250, cut_width=250):
    """
    切割圖片並儲存到指定目錄

    :param source_image_path: 原始圖片路徑
    :param output_dir: 輸出目錄
    :param cut_heigh: 切割高度，預設 250px
    :param cut_width: 切割寬度，預設 250px
    """
    # 讀取圖片
    picture = cv2.imread(image_path)

    # 取得圖片寬度、高度、深度
    width, height, depth = picture.shape

    # 預處理生成 0 矩陣
    pic = np.zeros((cut_height, cut_width, depth))

    # 計算切割數量
    width_count = int(width / cut_width)
    height_count = int(height / cut_height)

    for i in range(width_count):
        for j in range(height_count):
            # 計算切割的起始點
            start_x = i * cut_width
            start_y = j * cut_height

            # 計算切割的結束點
            end_x = (i + 1) * cut_width
            end_y = (j + 1) * cut_height

            # 切割圖片
            pic = picture[start_x:end_x, start_y:end_y]

            # 儲存圖片
            cv2.imwrite(f'{output_dir}cut_{i:02d}_{j:02d}.png', pic)

    print('圖片切割完成')

def combine_sprites(sprites_dir, output_image_path, height_count, width_count):
    """
    切割圖片並儲存到指定目錄

    :param sprites_dir: 動畫資料夾
    :param output_image_path: 輸出圖片路徑
    :param height_count: 高度個數
    :param width_count: 寬度個數
    :return combined_image: 合併後的圖片
    """
    # 讀取所有圖片檔案
    image_files = [f for f in os.listdir(sprites_dir) if f.endswith('.png')]
    print(f'找到 {len(image_files)} 張圖片。')

    # 確保圖片按順序排列
    image_files.sort()

    # 讀取第一張圖片以獲取尺寸
    first_image = cv2.imread(os.path.join(sprites_dir, image_files[0]))
    height, width, depth = first_image.shape
    print(f'圖片的寬: {width}, 高: {height}, 深度: {depth}。')

    # 創建一個空白的圖片以容納所有圖片
    combined_image = np.zeros((height*height_count, width*width_count, depth), dtype=np.uint8)

    pic_y = 0
    # 將每張圖片放入合併圖片中
    for i, image_file in enumerate(image_files):
        image = cv2.imread(os.path.join(sprites_dir, image_file))
        start_x = (i%width_count) * width
        end_x = start_x + width
        if i % width_count == 0 and i != 0:
            pic_y += height
        combined_image[pic_y:pic_y+250, start_x:end_x] = image

    # 儲存合併後的圖片
    cv2.imwrite(output_image_path, combined_image)
    print(f'合併圖片已儲存至 {output_image_path}')

    return combined_image
