import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Projects\C129\venv\C131 Data.csv')

name = df["Proper Name"].to_list()
mass = df["Mass (kg)"].to_list()
radius = df["Radius (m)"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity (m/s^2)"].to_list()

# Plot 1 - Name vs Mass
plt.figure(figsize=(10, 5))
plt.bar(name[0:9], mass[0:9])

plt.title("Stars Solar Mass")

# Plot 2 - Name vs Radius
plt.figure(figsize=(10, 5))
plt.bar(name[0:9], radius[0:9])

plt.title("Stars Solar Radius")

# Plot 3 - Name vs Distance
plt.figure(figsize=(10, 5))
plt.bar(name[0:9], dist[0:9])

plt.title("Stars Solar Distance")

# Plot 4 - Name vs Gravity
plt.figure(figsize=(10, 5))
plt.bar(name[0:9], gravity[0:9])

plt.title("Stars Solar Gravity")

plt.show()
