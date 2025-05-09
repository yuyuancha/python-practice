import cv2
from logic.image_tool import combine_sprites

image_path = './assets/default.png'
input_dir = './assets/sprites/'
result_image_path = './assets/combined_image.png'

# 讀取預設圖片檔案，取得預設圖片寬度、高度
default_picture = cv2.imread(image_path)
default_height, default_width, default_depth = default_picture.shape
print(f'預設圖片的寬: {default_width}, 高: {default_height}, 深度: {default_depth}。')

# 取得寬高個數
width_count = int(default_width / 250)
height_count = int(default_height / 250)
print(f'寬度切割數量: {width_count}, 高度切割數量: {height_count}, 總數量: {width_count * height_count}。')

combined_image = combine_sprites(input_dir, result_image_path, height_count, width_count)

# 顯示合併後的圖片
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
