<<<<<<< HEAD
import os
from dotenv import load_dotenv

import pandas as pd

file_location= os.getenv("file_location")
df = pd.read_csv(file_location)

#print(df.head(3))
print(df.shape)
=======
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
>>>>>>> 0b9f4a88f48d65697ea8028899bc49be19781e9c
