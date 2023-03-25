import pandas as pd

def pre_process_data(data):
    # convert csv data to pandas dataframe
    if(type(data) == str):
        df = pd.read_csv(data)
    if(type(data) == pd.DataFrame):
        df = data

    df.reset_index(drop=False, inplace=True)
    df.index = df.index.astype(int)

    df["time_idx"] = df.index 

    date_time = pd.to_datetime(df['Timestamp']).dt

    df["constant_group"] = "group_1"
    df['transaction_count'] = df['transaction_count'].astype(float)

    df["year"] = date_time.year
    df["month"] = date_time.month
    df["day"] = date_time.day
    df["hour"] = date_time.hour

    df['workforce_type_1'] = df['workforce_type_1'].astype(float)
    df['workforce_type_2'] = df['workforce_type_2'].astype(float)
    df['workforce_type_3'] = df['workforce_type_3'].astype(float)
    df['workforce_type_4'] = df['workforce_type_4'].astype(float)

    return df