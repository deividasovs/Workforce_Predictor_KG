import math

def convert_predictions_to_list(predictions):
    converted_predictions = [
    predictions[0][0].cpu().detach().numpy().tolist(),
    predictions[1][0].cpu().detach().numpy().tolist(),
    predictions[2][0].cpu().detach().numpy().tolist(),
    predictions[3][0].cpu().detach().numpy().tolist(),
    predictions[4][0].cpu().detach().numpy().tolist(),
    ]

    return converted_predictions

def ceil_round_predictions(predictions):
    for i in range(len(predictions)):
        if i > 0:
            for j in range(len(predictions[i])):
                predictions[i][j] = math.ceil(predictions[i][j])
        else:
            for j in range(len(predictions[i])):
                predictions[i][j] = round(predictions[i][j], 0)
            
    return predictions