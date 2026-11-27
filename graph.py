import numpy as np
import matplotlib.pyplot as plt

Th = 300.0    # hot end (K)
Tc = 4.0      # cold end (K)
L = 0.5       # length (m)
k = 400.0     # conductivity (W/m.K)
A = 1e-6      # area (m^2)

x = np.linspace(0, L, 51)         # 51 points, 0 se L tak
T = Th + (Tc - Th) * x / L        # analytic formula

Q = k * A * (Th - Tc) / L
print("Q =", Q, "W")              # ~0.237 aana chahiye

plt.plot(x, T, label="analytic T(x)")
plt.xlabel("x (m)")
plt.ylabel("Temperature (K)")
plt.title("Constant-k rod, analytic")
plt.legend()
plt.grid(True)
plt.show()