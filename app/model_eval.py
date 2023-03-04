from data_preprocessing import pre_process_data
import matplotlib.pyplot as plt
from pytorch_forecasting import  TemporalFusionTransformer

#modelPath = "./app/saved_models/bestCheckpoint1.pth"
# ./lightning_logs/version_3/checkpoints/epoch=2-step=90.ckpt" when deploying!
modelPath = "./app/lightning_logs/version_36/checkpoints/epoch=20-step=630.ckpt"

def get_prediction(data):
    # For testing purposes, should be created otherwise
    #./test_new_data1.csv when deploying!
    #test_data = "./test_new_data1.csv"
    #data = pre_process_data(test_data)
    
    #data = pre_process_data(data)

    saved_tft = TemporalFusionTransformer.load_from_checkpoint(modelPath)

    predictions = saved_tft.predict(data)

    # Raw predictions for plotting purposes
    #raw_predictions, x = saved_tft.predict(data, mode="raw", return_x=True, show_progress_bar=True

    #saved_tft.plot_prediction(x, raw_predictions, idx=0)

    # plt.show only the first 200 samples
    #plt.xlim(-100, 80)
    #plt.savefig("./app/Graphs/ReturnedGraph.png")

    # Only tmp seems to be writable
    # https://stackoverflow.com/a/42002539/6114105

    # Could also return loss & more complex graphs
    #with open("/tmp/ReturnedGraph.png", "rb") as f:
    #with open("./app/Graphs/ReturnedGraph.png", "rb") as f:
    #    image = f.read()
    #    image = base64.b64encode(image).decode('utf-8')

    #return predictions, image
    return predictions


# For testing purposes
if __name__ == "__main__":
    # load csv file to variable test_data
    test_data = "./app/test_new_data1.csv" # TODO: New test data, this was trained on!
    #test_data = "./app/xMonths_SimulatedStaff.csv"
    predictions  = get_prediction(test_data)

    predictionResults = [predictions[0].cpu().detach().numpy(), predictions[1].cpu().detach().numpy()]