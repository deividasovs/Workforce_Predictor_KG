import math

def predictionsToList(predictions):
    convertedPredictions = [
    predictions[0][0].cpu().detach().numpy().tolist(),
    predictions[1][0].cpu().detach().numpy().tolist(),
    predictions[2][0].cpu().detach().numpy().tolist(),
    predictions[3][0].cpu().detach().numpy().tolist(),
    predictions[4][0].cpu().detach().numpy().tolist(),
    ]

    return convertedPredictions

def ceilRoundPredictions(predictions):
    for i in range(len(predictions)):
        if i > 0:
            for j in range(len(predictions[i])):
                predictions[i][j] = math.ceil(predictions[i][j])
        else:
            #print(predictions[0])
            for j in range(len(predictions[i])):
                predictions[i][j] = round(predictions[i][j], 0)
            
    return predictions