import csv
import pandas as pd

df = pd.read_csv(r'Projects\C129\venv\C130 DataCleaning.csv')

mass_old = df["Solar Mass"].to_list()
radius_old = df["Solar Radius"].to_list()

mass_new = []
radius_new = []
gravity_list = []

for mass in mass_old:
    mass = mass * 1.989e+30
    mass_new.append(mass)


for radius in radius_old:
    radius = radius * 6.957e+8
    radius_new.append(radius)


gravity_const = float(6.67e-11)
for index in range(len(mass_old)):
    gravity_temp = gravity_const * \
        (float(mass_new[index]) / float(radius_old[index] ** 2))

    gravity_list.append(gravity_temp)

gravity_df = pd.DataFrame({
    'Mass (kg)': mass_new,
    'Radius (m)': radius_new,
    'Gravity (m/s^2)': gravity_list
})

latest_df = pd.concat([df, gravity_df], axis=1)
print(latest_df)
