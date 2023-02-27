import torch.nn as nn

a, b = 24, 12


class MultiLayerMultiLabelRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(MultiLayerMultiLabelRegression, self).__init__()
        self.linear = nn.Linear(input_size, a)
        self.linear = nn.Linear(a, b)
        self.dropout = nn.Dropout(0.5)
        self.relu = nn.ReLU()
        self.linear = nn.Linear(b, output_size)

    def forward(self, x):
        out = self.linear(out)
        out = nn.ReLU()
        out = self.linear(out)
        out = self.dropout(out)
        out = self.linear(out)
        return out
