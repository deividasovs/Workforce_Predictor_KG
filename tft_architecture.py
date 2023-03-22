from pytorch_forecasting import TemporalFusionTransformer, TimeSeriesDataSet
from pytorch_forecasting.metrics import QuantileLoss, MultiLoss
from ipynb.fs.full.training_preprocessing import get_dataset

df = get_dataset()

max_prediction_length = 9*7  # How many datapoints will be predicted (~1 week)
max_encoder_length = 9*60  # Determines the look back period (~2 months)

training_cutoff = df["time_idx"].max()  # Will need to modify this

training = TimeSeriesDataSet(
    df[lambda x: x['time_idx'] <= training_cutoff],
    time_idx="time_idx",
    target=["transaction_count", "workforce_type_1",
            "workforce_type_2", "workforce_type_3", "workforce_type_4"],
    # weight="weight",
    group_ids=["constant_group"],
    max_encoder_length=max_encoder_length,
    min_encoder_length=max_encoder_length // 2,
    max_prediction_length=max_prediction_length,
    static_reals=[],
    # List of categorical variables that do not change over time
    static_categoricals=['constant_group'],
    # List of categorical variables that change over time and are known in the future
    time_varying_known_categoricals=[],
    time_varying_unknown_categoricals=[],
    # list of continuous variables that change over time and are known in the future
    time_varying_known_reals=["time_idx", 'holiday', 'rain',
                              'temperature', 'hour', 'year', 'month', 'day'],
    time_varying_unknown_reals=[
        "subtotal",
        "transaction_count",
        "oil_price",
        "workforce_type_1",
        "workforce_type_2",
        "workforce_type_3",
        "workforce_type_4",
    ],
)


# create validation and training dataset
batch_size = 128

validation = TimeSeriesDataSet.from_dataset(
    training, df, min_prediction_idx=training.index.time.max() + 1, stop_randomization=True)

train_dataloader = training.to_dataloader(
    train=True, batch_size=batch_size, num_workers=8)

val_dataloader = validation.to_dataloader(
    train=False, batch_size=batch_size, num_workers=8)

# create the model
tft = TemporalFusionTransformer.from_dataset(
    training,
    learning_rate=0.01,
    hidden_size=32,
    attention_head_size=1,
    dropout=0.1,
    hidden_continuous_size=16,
    output_size=[7, 7, 7, 7, 7],
    loss=MultiLoss([QuantileLoss(), QuantileLoss(),
                   QuantileLoss(), QuantileLoss(), QuantileLoss()]),
    log_interval=2,
    reduce_on_plateau_patience=4
)
print(f"Number of parameters in network: {tft.size()/1e3:.1f}k")
