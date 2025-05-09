from logic.video_tool import generate_animation_sprites

# video_path = './assets/slow_motion/siterle_16.mp4'  # 希特勒貓貓
video_path = './assets/slow_motion/oiioi_16.mp4'  # 51121貓貓
screenshot_root = './assets/screenshot/'  # 截圖儲存根目錄
# screenshot_dir = 'walk'  # 截圖儲存資料夾名稱
screenshot_dir = 'stand'  # 截圖儲存資料夾名稱
count = 8

generate_animation_sprites(screenshot_dir, video_path, count=count)
