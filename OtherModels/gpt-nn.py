import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

# Load the data from the CSV file
df = pd.read_csv('../Data_Manipulation/Data/xMonths_SimulatedStaff.csv')
#df = pd.read_csv("transactions.csv")

# Convert the data to tensors
subtotal = torch.tensor(df['subtotal'].values, dtype=torch.float)
transaction_count = torch.tensor(
    df['transaction_count'].values, dtype=torch.float)
temperature = torch.tensor(df['temperature'].values, dtype=torch.float)
#timestamp = torch.tensor(df['Timestamp'].values, dtype=torch.float)

# Define the model


class StaffForecaster(nn.Module):
    def __init__(self):
        super(StaffForecaster, self).__init__()
        self.fc1 = nn.Linear(3, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64, 128)
        self.fc4 = nn.Linear(128, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


# Instantiate the model
model = StaffForecaster()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
for i in range(1000):
    # Forward pass
    output = model(
        torch.cat((subtotal, transaction_count, temperature), dim=0))

    # Compute loss and backpropagate
    loss = criterion(output, timestamp)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Test the model on new data
test_subtotal = torch.tensor([100.0, 200.0, 300.0])
test_transaction_count = torch.tensor([1.0, 2.0, 3.0])
test_temperature = torch.tensor([60.0, 70.0, 80.0])

test_output = model(
    torch.cat((test_subtotal, test_transaction_count, test_temperature), dim=1))
print(test_output)