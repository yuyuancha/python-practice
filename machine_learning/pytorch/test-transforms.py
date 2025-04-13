import cv2
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "./assets/hymenoptera_data/train/ants/0013035.jpg"
img = cv2.imread(img_path)

writer = SummaryWriter("logs")

tensor_transforms = transforms.ToTensor()
tensor_img = tensor_transforms(img)

writer.add_image("tensor img", tensor_img, 1)

writer.close()
