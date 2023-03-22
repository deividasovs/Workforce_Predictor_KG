
import requests
from model_eval import get_prediction
from data_postprocessing import convert_predictions_to_list, ceil_round_predictions
import pandas as pd

import json

#TEST_DYNAMIC_DATA_ENDPOINT = "http://127.0.0.1:8000/CreateDynamicDataset"
DYNAMIC_DATA_ENDPOINT = "https://eh3xvfep7ae75yaor75tdpkv3q0wkszs.lambda-url.eu-west-1.on.aws/"

# testing note:
# host on port 8080 when testing locally
# sam local start-api -p 8080

# This is run every Sunday to generate the Data and forecasts for the next week
def lambda_handler(event, context):
    input_data = requests.get(DYNAMIC_DATA_ENDPOINT).json()

    df_input_data = pd.DataFrame(input_data)

    predictions = get_prediction(df_input_data)

    predictions = convert_predictions_to_list(predictions)
    predictions = ceil_round_predictions(predictions)

    response_body = {
                "transaction_count": predictions[0],
                "dept1": predictions[1],
                "dept2": predictions[2],
                "dept3": predictions[3],
                "dept4": predictions[4],
            }


    response_body = json.dumps(response_body)

    return {
        'statusCode': 200,
        'body': response_body,
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
    response = json.loads(response['body'])
    
    with open("data.json", "w") as outfile:
        json.dump(response, outfile)

    print(response['transaction_count'])