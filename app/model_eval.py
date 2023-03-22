from data_preprocessing import pre_process_data
from pytorch_forecasting import  TemporalFusionTransformer

modelPath = "./app/lightning_logs/version_36/checkpoints/epoch=20-step=630.ckpt"

def get_prediction(data):
    data = pre_process_data(data)

    saved_tft = TemporalFusionTransformer.load_from_checkpoint(modelPath)

    predictions = saved_tft.predict(data)

    return predictions