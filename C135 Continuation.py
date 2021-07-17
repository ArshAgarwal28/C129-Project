import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Projects\C129\venv\C131 Data.csv')
df2 = df[["Proper Name", "Mass (kg)", "Radius", "Distance", "Gravity (m/s^2)"]]

# Plot 1 - Name vs Mass
plt.subplot(2, 2, 1)
plt.plot(df2["Proper Name"], df2["Mass (kg)"], '--b')

plt.title("Star Name and Mass")
# plt.xlabel("Star Name")
# plt.ylabel("Mass")


# Plot 2 - Name vs Radius
plt.subplot(2, 2, 2)
plt.plot(df2["Proper Name"], df2["Radius"], '--b')

plt.title("Star Name and Radius")
# plt.xlabel("Star Name")
# plt.ylabel("Radius")


# Plot 3 - Name vs Distance
plt.subplot(2, 2, 3)
plt.plot(df2["Proper Name"], df2["Distance"], '--b')

plt.title("Star Name and Distance")
# plt.xlabel("Star Name")
# plt.ylabel("Distance")


# Plot 2 - Name vs Gravity
plt.subplot(2, 2, 4)
plt.plot(df2["Proper Name"], df2["Gravity (m/s^2)"], '--b')

plt.title("Star Name and Gravity")
# plt.xlabel("Star Name")
# plt.ylabel("Gravity")

plt.show()
