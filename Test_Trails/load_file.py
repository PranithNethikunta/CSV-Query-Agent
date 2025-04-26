import pandas as pd

def load_dataframe(file_location):
    try:
        df=pd.read_csv(file_location)
        print("Data is loaded into dataframe sucessfully")
        print(df.head())
        return df
    except Exception as e:
        print("error loading CSV file")
        return None