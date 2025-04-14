import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

train_set = torchvision.datasets.MNIST(root="./datasets", train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.MNIST(root="./datasets", train=False, transform=dataset_transform, download=True)

writer = SummaryWriter("logs")

print("train_set length:", len(train_set))
print("test_set length:", len(test_set))

for i in range(10):
    img, target = train_set[i]
    writer.add_image("train_set", img, i)

for i in range(10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)

writer.close()
