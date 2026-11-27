import sympy as sp

def summation_function():
    try:
        A = float(input("ENTER SUMMATION STARTING LIMIT: "))
        if A < 0:
            
            raise ValueError("Starting limit cannot be negative")
        if A == "":
            raise ValueError("Starting limit cannot be empty")
        B = float(input("ENTER SUMMATION ENDING LIMIT: "))
        if B < A:
            raise ValueError("Ending limit must be greater than or equal to starting limit")
        if B == "":
            raise ValueError("Number of steps cannot be empty")
        n = int(input("ENTER NUMBER OF STEPS: "))
        if n <= 0:
            raise ValueError("Number of steps must be positive")
        if n == "":
            raise ValueError("Number of steps cannot be empty")
    
    except ValueError as e:
        print(f"ERROR: {e}")
        return None
    try:
        fx_string = input("ENTER FUNCTION (use 'x' as variable): ")
    except ValueError as e:
        print(f"ERROR: {e}")
        return None

    # SymPy se function parse karo
    x = sp.Symbol('x')
    try:
        expr = sp.sympify(fx_string)
    except sp.SympifyError:
        print("ERROR: Invalid function")
        return None

    # Fast numerical evaluation ke liye convert
    f = sp.lambdify(x, expr, 'math')

    dx = (B - A) / n
    total_sum = 0.0

    # for loop — floating point issue nahi
    for i in range(n):
        xi = A + i * dx          # left endpoint
        total_sum += f(xi) * dx

    print(f"\nIntegral ≈ {total_sum}")
    return total_sum


if __name__ == "__main__":
    summation_function()