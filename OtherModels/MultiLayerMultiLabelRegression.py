import torch.nn as nn

a,b = 12,8

class MultiLayerMultiLabelRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(MultiLayerMultiLabelRegression, self).__init__()
        self.linear1 = nn.Linear(input_size, a)
        self.linear2 = nn.Linear(a, b)
        self.dropout = nn.Dropout(0.3)
        self.linear3 = nn.Linear(b, output_size)

    def forward(self, x):
        out = self.linear1(x)
        out = self.linear2(out)
        out = self.dropout(out)
        out = self.linear3(out)
        return out