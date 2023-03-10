import torch.nn as nn

class MultiLabelRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(MultiLabelRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
    
    def forward(self, x):
        out = self.linear(x)
        return out
