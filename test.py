from time import clock, monotonic

import torch

import datetime
from time import sleep

a = datetime.datetime.now()

x = torch.rand([2000, 3000])
y = (x - x + x * 10.0) ** 2
b = datetime.datetime.now()
delta = b - a
print(delta.microseconds)
