import os
import torch
from torch import nn
from torch.utils.data import DataLoader

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using " + device)

class testCnn(nn.Module):
    def __init__(self):
        super(testCnn, self).__init__()
        self.flatten = nn.Flatten()
        self.reluStack = nn.Sequential(
            nn.Linear((28*28), 512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,1)
        )
