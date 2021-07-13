import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'Projects\C129\venv\C131 Data.csv')


def star_less_hundred(x):
    if x <= 100:
        return x

    return np.nan


def gravity_range(x):
    if x > 150 and x < 350:
        return x

    return np.nan


df2 = pd.DataFrame(columns=["Distance", "Gravity"])

df2["Distance"] = df["Distance"].apply(star_less_hundred)
df2["Gravity"] = df["Gravity (m/s^2)"].apply(gravity_range)

print(df2)
