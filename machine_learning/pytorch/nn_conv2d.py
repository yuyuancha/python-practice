from torch.utils.data import DataLoader

datasets = torchvision.datasets.CIFAR10("./datasets", train=False, transform=torchvision.transforms.ToTensor(), download=True)
