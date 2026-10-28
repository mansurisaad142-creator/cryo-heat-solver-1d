import math

def getk(T):
    """Returns thermal conductivity of copper at temperature T (in K)"""
    if T > 100:
        return 400
    elif 4 <= T <= 100:
        return 1000
    elif T < 4:
        return 50

# Wire parameters
A = 1e-6  # cross-sectional area (m^2)
L = 0.1   # length (m)
T_cold = 4   # cold end temperature (K)
T_hot = 300  # hot end temperature (K)

# Numerical integration using Riemann summation
# We integrate 1/k(T) from T_cold to T_hot
total_sum = 0
dT = 0.1  # temperature step
T = T_cold

while T <= T_hot:
    k = getk(T)
    inverse_k = 1 / k
    total_sum += inverse_k * dT
    T += dT

# Calculate heat flow Q
# Q = A / (L * integral of 1/k(T) dT)
Q = A / (L * total_sum)

print(f"Integral of 1/k(T) from {T_cold}K to {T_hot}K: {total_sum:.6f}")
print(f"Heat flow Q: {Q:.6f} Watts")
