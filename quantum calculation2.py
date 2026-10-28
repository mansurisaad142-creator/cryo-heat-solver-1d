import math

def summation_function():
    # Convert inputs to float so users can enter decimals if they want
    A = float(input("ENTER SUMMATION STARTING LIMIT: "))
    B = float(input("ENTER SUMMATION ENDING LIMIT: "))
    
    total_sum = 0
    dx = float(input("enter dx value or enter strip number for area: "))
    
    fx_string_storer = getK(T)

    # Start x at the initial limit A
    x = A
    
    # Using a while loop allows us to step by small decimals (dx)
    # We add dx/2 to B to avoid floating-point rounding errors cutting off the last step
    while x <= (B):
        
        # Evaluate the string formula using the current value of x
        
        
        # For true integration/summation, we multiply the height f(x) by the width (dx)
        # If you only want pure summation without dx, just remove "* dx"
        current_value = fx_string_storer * dx
        total_sum += current_value
        
        print(f"X = {x:.2f} | F(X) VALUE = {fx_real_formula:.4f}") 
        print(f"TOTAL SUMMATION SO FAR = {total_sum:.4f}")
        print("=" * 65)
        
        # Increment x by the small step dx
        x += dx
        
    return total_sum

summation_function()
