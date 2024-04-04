"""
数据归一化处理
使用torch求均值与标准差
"""

import os
from torchvision.datasets import ImageFolder
import torch
from torchvision import transforms as T
from tqdm import tqdm

transform = T.Compose([
     T.RandomResizedCrop(224),
     T.ToTensor(),
])

def getStat(train_data):
    train_loader = torch.utils.data.DataLoader(
        train_data, batch_size=1, shuffle=False, num_workers=0, pin_memory=True)

    mean = torch.zeros(3)
    std = torch.zeros(3)
    for X, _ in tqdm(train_loader):
        for d in range(3):
            mean[d] += X[:, d, :, :].mean() # N, C, H ,W
            std[d] += X[:, d, :, :].std()
    mean.div_(len(train_data))
    std.div_(len(train_data))
    return list(mean.numpy()), list(std.numpy())


if __name__ == '__main__':
    # 检查enhance_dataset是否存在，如果不存在则使用dataset
    root = r'enhance_dataset' if os.path.exists(r'enhance_dataset') else r'dataset'

    train_dataset = ImageFolder(root=root, transform=transform)
    print(getStat(train_dataset))