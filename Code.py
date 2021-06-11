import pandas as pd
import csv

from pandas.core.reshape.merge import merge

planet_data = []

with open(r'Projects\C128\venv\data.csv', 'r', encoding="utf-8") as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        if row != []:
            planet_data.append(row)

headers = planet_data[0]
planets_data = planet_data[1:]
planets_data.pop(-1)

new_values = []
for planet in planets_data:
    solar_mass = planet[2].replace('', '0')
    solar_radius = planet[3].replace('', '0')

    try:
        solar_radius = int(float(solar_radius)) * 0.102763
        solar_mass = int(float(solar_mass)) * 0.000954588
    except:
        print(planet)

    new_values.append([solar_mass, solar_radius])

new_df = pd.DataFrame(new_values, columns=['Solar Mass', 'Solar Radius'])
print(new_df)
# prev_df = pd.read_csv(r'Projects\C128\venv\data.csv')

# df_merged = pd.concat([prev_df, new_df], ignore_index=True)
# print(df_merged)

# df_merged.to_csv(r'Projects\C129\venv\final.csv')
