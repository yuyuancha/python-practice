# import torch
from PIL import Image

img_path = "./hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)
img.show()

# device = torch.device("mps")
# print(torch.cuda.is_available())
# print(torch.backends.mps.is_available())

# print(dir(torch))
# print(help(torch.backends.mps.is_available))
