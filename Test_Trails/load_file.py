import os
from dotenv import load_dotenv

import pandas as pd

file_location= os.getenv("file_location")
df = pd.read_csv(file_location)

#print(df.head(3))
print(df.shape)