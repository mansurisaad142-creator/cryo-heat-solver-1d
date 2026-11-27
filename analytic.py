def heat_rate(k, A, L, T_hot, T_cold):
    return k * A * (T_hot - T_cold) / L

def thermal_resistance(k, A, L):
    return L / (k * A)