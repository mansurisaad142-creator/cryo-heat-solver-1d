import numpy as np
import matplotlib.pyplot as plt


def get_input():
    K = float(input("Enter the value of K(unit W/m.K): ")) # W/m.K # thermal conductivity of the material
    A = float(input("Enter the value of A(unit m^2): ")) # m^2 # wire cross sectional area
    L = float(input("Enter the value of L(unit m): ")) # m # wire length
    T_hot = float(input("Enter the value of T_hot(unit K): ")) # K # hot temperature
    T_cold = float(input("Enter the value of T_cold(unit K): ")) # K # cold temperature
    position = float(input("Enter the position (m): "))
    return K, A, L, T_hot, T_cold, position

def  plot_temperature_distribution(K,A, L, T_hot, T_cold):
    n=np.linspace(0, L, 100) # 0 se 0.5 m tak 100 barabar doori wale points. Matlab taar par 100 jagahein jahan hum temperature dekhenge.
    # hum 100 points par temperature calculate kar rahe hain 
    T=T_hot - (T_hot - T_cold) * n / L # T is the temperature distribution across the wire  
    # formula for temperature distribution
    plt.plot(n, T) # plot the temperature distribution
    plt.xlabel("Length (m)")
    plt.ylabel("Temperature (K)")
    plt.title("Temperature Distribution")
    plt.grid(True)
    plt.savefig("temperature_distribution.png", dpi=150, bbox_inches="tight")# ye  image mvp 0.05 folder me save kar dega
    plt.show() # show the plot

def heat_rate(K, A, L, T_hot, T_cold):
    Q = K * A * (T_hot - T_cold) / L # Q is the heat transfer rate
    print("The heat transfer rate is:", Q, "W") # print the heat transfer rate
    return Q


def temperature_on_point(K, A, L, T_hot, T_cold, position):

    T = T_hot - (T_hot - T_cold) * position / L # T is the temperature at point x
    print("The temperature at point ", position, " m is:", T, "K") # print the temperature at point x
    return T


def thermal_resistance(K, A, L):
    R = L / (K * A)
    print("The thermal resistance is:", R, "K/W")
    return R

if __name__ == "__main__":
    K, A, L, T_hot, T_cold , position = get_input()
    plot_temperature_distribution(K, A, L, T_hot, T_cold)
    heat_rate(K, A, L, T_hot, T_cold)
    temperature_on_point(K, A, L, T_hot, T_cold , position)
    thermal_resistance(K, A, L)

