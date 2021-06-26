from Merge import star_data_df as df

import pandas as pd


del df["Luminosity"]
df.dropna(inplace=True)

df.to_csv(r'Projects\C129\venv\C130 DataCleaning.csv', index=False)
