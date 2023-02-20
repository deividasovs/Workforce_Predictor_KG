import numpy as np
import pandas as pd


def pre_process_data(data):
    # convert csv data to pandas dataframe
    if(type(data) == str):
        df = pd.read_csv(data)
    if(type(data) == pd.DataFrame):
        df = data

    df["time_idx"] = df.index  # TODO: turn this into some maths function?

    dateTime = pd.to_datetime(df['Timestamp']).dt

    df["constant_group"] = "group_1"
    df['transaction_count'] = df['transaction_count'].astype(float)

    df["year"] = dateTime.year
    df["month"] = dateTime.month
    df["day"] = dateTime.day
    df["hour"] = dateTime.hour

    df['workforce_type_1'] = df['workforce_type_1'].astype(float)
    df['workforce_type_2'] = df['workforce_type_2'].astype(float)
    df['workforce_type_3'] = df['workforce_type_3'].astype(float)
    df['workforce_type_4'] = df['workforce_type_4'].astype(float)

#    print(df)
    return df