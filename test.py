import torch

x = torch.tensor(
    [[1., 2., 3., 4.],
     [5., 6., 7., 8.],
     [9., 10., 11., 12.]], requires_grad=True)

function = 10 * (x ** 2).sum()

function.backward()

print(x.grad, '<- gradient')
