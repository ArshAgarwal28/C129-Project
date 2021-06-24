import csv
import pandas as pd

df = pd.read_csv(r'Projects\C129\venv\BrownDwarf.csv')

df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

mass = df["Mass"].tolist()
solar_mass_values = []

radius = df["Radius"].tolist()
solar_radius_values = []

for mass_val in df["Mass"]:
    new_mass_val = float(mass_val) * 0.000954588
    solar_mass_values.append(new_mass_val)

for radius_val in df["Radius"]:
    new_rad_val = float(radius_val) * 0.102763
    solar_radius_values.append(new_rad_val)


df = df.replace(mass, solar_mass_values)
df = df.replace(radius, solar_radius_values)

df.to_csv(r'Projects\C129\venv\NewSolarUpdated.csv',
          index=False, header=['Constellation', 'Distance', 'Solar Mass', 'Solar Radius'])
# for count, radius in enumerate(df["Radius"]):
#     solar_rad_val = float(radius) * 0.102763
#     df.at[count, 'Radius'] = solar_rad_val
