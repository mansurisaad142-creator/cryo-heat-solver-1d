import math
import numpy as np

# =================================================================
# 1. FORCE CALCULATOR SUB-ROUTINE
# =================================================================
def force_calculator():
    print("\n--- FORCE CALCULATOR ENGINE ---")
    mass_input = int(input("MASS(IN KG): "))
    accel_input = int(input("ACCELERATION(IN M/SEC^-2) : "))
    
    # The calculation must sit inside the function scope
    force = mass_input * accel_input 
    print("FORCE IS =", force, "NEWTON")
    return force

# =================================================================
# 2. STRESS SOLVER SUB-ROUTINE
# =================================================================
def stress_solver():
    print("\n--- STRESS SOLVER ENGINE ---")
    start = int(input("STARTING LIMIT OF FORCE(INN)     = "))
    end = int(input("ENDING LIMIT OF FORCE(INN)        = "))
    A = int(input("ENTER RADIUS:(IN CM)="))
    
    B = math.pi
    C = B * A**2
    print("AREA OF CIRCLE IS(IN CM)=", C)
    stress_limit = float(input("ENDING LIMIT OF MATERIAL STRESS(IN N/M^2): "))

    if C == 0:
        print("NOT ALLOWED")
    else: 
        for force in range(start, end):
            stress = force / C
            print('STRESS=', stress)       
            if stress >= stress_limit:
                print("DANGER")
                break
                
    return None # We return nothing because we already printed the states

# =================================================================
# 3. ENERGY SOLVER SUB-ROUTINE
# =================================================================
def energy_solver():
    print("\n--- ENERGY SOLVER ENGINE ---")
    print("=" * 60)
    m = (np.array([(int(input("Enter mass: ".upper())))]))
    h = np.array([int(input("Enter height: ".upper()))])
    v = np.array([int(input("Enter velocity:".upper()))])
    diameter = np.array([int(input("Enter diameter:".upper()))])
    force = np.array([int(input("Enter force: ".upper()))])
    
    PE = 9.8 * m * h
    KE = 0.5 * m * v**2
    area = np.pi * (diameter / 2)**2
    stress = force / area
    
    print('KE=', KE, 'KGM**2')
    print('PE=', PE, 'KGM**2SEC**2')
    print('STRESS=', stress, 'KGM**-1SEC**2')
    print("=" * 60)
    return KE, PE, stress

# =================================================================
# 4. PRIMARY CONTROLLER LOGIC ENGINE
# =================================================================
def main():
    while True:
        print('\n============================================================')
        print("MY PHYSICS CODEBASE")
        print('============================================================')
        print("1.force_calculator")
        print("2.stress_solver")
        print("3.energy_solver")
        print("4.exit")
        print('============================================================')
        
        choice = input('CHOOSE: ').strip()
        
        if choice == '1':
            force_calculator()
        elif choice == '2':
            stress_solver()
        elif choice == '3':
            energy_solver()
        elif choice == '4':
            print("CLOSING ARCHITECTURE SYSTEM.")
            break
        else:
            print("☠️ INVALID CHOICE Loop CONTINUES.")

if __name__ == "__main__":
    main()
    