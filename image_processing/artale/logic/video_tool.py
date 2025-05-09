import cv2
import os
from . import tool

def generate_animation_sprites(dir_name, video_path, count=10):
    screenshot_root = './assets/screenshot/'
    tool.create_when_not_existed(screenshot_root)

    dir_name = os.path.join(screenshot_root, dir_name)
    tool.create_when_not_existed(dir_name)

    cap = cv2.VideoCapture(video_path)  # 開啟影片檔案
    screenshot_count = 0 # 截圖計數器
    min_frames = 50 # 最小幀數限制

    if not cap.isOpened():
        print("無法開啟影片檔案")
        exit()

    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"影片總幀數: {total_frames}")

    if total_frames < min_frames:
        print("影片幀數不足，無法截圖")
        exit()

    total_frames = total_frames - min_frames

    cut_frame = int(total_frames / count)
    print(f"每段影片幀數: {cut_frame}")

    frames_list = []
    for i in range(count):
        frames_list.append(int(i * cut_frame))
    print(f"每段影片幀數: {frames_list}")

    for frame in frames_list:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, frame = cap.read()
        if not ret:
            print("無法讀取影片幀")
            break
        screenshot_count += 1
        filename = f"{dir_name}/{screenshot_count}.png"
        cv2.imwrite(filename, frame)
        print(f"已儲存截圖: {filename}")

    cap.release()
    cv2.destroyAllWindows()

def generate_slow_motion(video_name, slow_factor=16):
    output_dir = './assets/slow_motion/'
    tool.create_when_not_existed(output_dir)

    output_path = os.path.join(output_dir, f'{video_name}_{slow_factor}.mp4')
    video_path = os.path.join('./assets/videos/', f'{video_name}.mp4')

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 保持原幀率，重複幀實現慢動作
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 重複多次寫入
        for _ in range(slow_factor):
            out.write(frame)

    cap.release()
    out.release()
    print("慢動作影片已儲存。")
