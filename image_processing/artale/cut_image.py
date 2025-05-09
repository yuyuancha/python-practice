import cv2
import numpy as np
import os
from logic.image_tool import cut_image_and_save

image_path = './assets/default.png'
output_dir = './assets/sprites/'
cut_width = 250
cut_height = 250

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cut_image_and_save(image_path, output_dir, cut_height=cut_height, cut_width=cut_width)
