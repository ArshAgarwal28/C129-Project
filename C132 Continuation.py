from C131_Continuation import latest_df as df

import matplotlib.pyplot as plt
import numpy as np

mass_list = sorted(df["Mass (kg)"].tolist())
radius_list = sorted(df["Radius (m)"].tolist())
gravity_list = sorted(df["Gravity (m/s^2)"].tolist())

# Plot 1
plt.subplot(1, 2, 1)
plt.plot(mass_list, radius_list, '--b')

plt.title("Mass and Radius")
plt.xlabel("Mass")
plt.ylabel("Radius")

# Plot 2
plt.subplot(1, 2, 2)
plt.plot(mass_list, gravity_list, ':r')

plt.title("Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")

plt.show()
