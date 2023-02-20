# Create new data to be filled with available online sources
# Create a df with the same columns as the training data
#
import pandas as pd
from data_preprocessing import pre_process_data


"""
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


"""


def createNewData():

    # TODO: Put the data frame through the data preprocessor!
    df = pd.DataFrame(
        columns=['Timestamp', 'transaction_count', "oil_price", "subtotal", "holiday", "rain", "temperature",
                 'workforce_type_1', 'workforce_type_2', 'workforce_type_3', 'workforce_type_4']
    )

    # convert timestamp column to datetime
    # df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Add rows for the next 7 days
    # next 7 days
    i = 0
    # df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # for d in range(7):
    for d in range(8):
        # x hours per day
        for h in range(10, 19):
            # for each d day and h hour, add a row, setting the d as the offset from today and h as the hour in the timestamp column
            # df.loc[i] = ['Timestamp': pd.to_datetime('today') + pd.DateOffset(days=d), 'transaction_count': 0, 'oil_price': 0, 'subtotal': 0, 'holiday': 0, 'rain': 0, 'temperature': 0, 'workforce_type_1': 0, 'workforce_type_2': 0, 'workforce_type_3': 0, 'workforce_type_4': 0]
            df.loc[i] = [pd.to_datetime(
                'today') + pd.DateOffset(days=d), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # set the hour to h
            df.loc[i, 'Timestamp'] = df['Timestamp'][i].strftime(
                '%Y-%m-%d ' + str(h) + ':00:00')

            i += 1

    df = pre_process_data(df)

    # print(df)

    return df


if __name__ == "__main__":
    createNewData()
