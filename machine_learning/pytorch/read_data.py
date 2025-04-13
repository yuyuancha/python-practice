from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path_list = os.listdir(self.path)

    def __len__(self):
        return len(self.img_path_list)

    def __getitem__(self, idx):
        name = self.img_path_list[idx]
        path = os.path.join(self.root_dir, self.label_dir, name)
        img = Image.open(path)
        label = self.label_dir
        return img, label
