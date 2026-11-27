import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 0.5  # Length of the wire in meters
T_hot = 100  # Temperature at the hot end in Kelvin
T_cold = 300  # Temperature at the cold end in Kelvin
K = 100  # Thermal conductivity in W/(m·K)
A = 0.01  # Cross-sectional area in m²

n = np.linspace(0, L, 100)
T = T_hot-(T_hot - T_cold) * n / L
plt.plot(n , T)
plt.xlabel("Length (m)")
plt.ylabel("Temperature (K)")
plt.title("Temperature Distribution")
plt.grid(True)
plt.savefig("temperature_distribution.png")
plt.show()

Q = K * A *(T_hot - T_cold)/L
print("The heat transfer rate is:", Q, "W")
