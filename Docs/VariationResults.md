# Variations
Baseline values:


## 1. TFT
### Specs:
Preprocessing

#### Hyper parameters
max_prediction_length = 9*7 # How many datapoints will be predicted (~1 week)
max_encoder_length = 9*60 # Determines the look back period (~2 months)

training_cutoff = df["time_idx"].max()  # Will need to modify this



learning_rate = 0.03


run time = 15 mins -- Keep it constant for all?

#### Results
Mean absolute error rate = 7.76


## 2. Neural Net