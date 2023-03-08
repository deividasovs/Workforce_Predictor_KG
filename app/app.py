import requests
from model_eval import get_prediction
from data_postprocessing import predictionsToList, ceilRoundPredictions

from new_data import createNewData

import json

def lambda_handler(event, context):
    # fetch input data from data creator api https://some-link.com
    input_data = requests.get("https://some-link.com").json()

    #predictions, image = get_prediction(input_data) Use to return the performance of the graph
    predictions = get_prediction(input_data)

    predictions = predictionsToList(predictions)
    predictions = ceilRoundPredictions(predictions)

    responseBody = {
                #"image": image,
                "transaction_count": predictions[0],
                "dept1": predictions[1],
                "dept2": predictions[2],
                "dept3": predictions[3],
                "dept4": predictions[4],
            }


    responseBody = json.dumps(responseBody)

    return {
        'statusCode': 200,
        'body': responseBody,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent',
            'Content-Type': 'application/json',
        }
    }


# For testing purposes
if __name__ == "__main__":
    response = lambda_handler(None, None)

    # convert response string to json
    response = json.loads(response['body'])

    print(response['transaction_count'])