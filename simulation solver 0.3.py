import numpy as np
import sys

def get_matrix_input(dim: int) -> tuple[np.ndarray, np.ndarray]:
    """Dynamically parses multi-line user input into validated NumPy arrays."""
    print(f"\nEnter the {dim}x{dim} Matrix A (space-separated numbers for each row):")
    a_rows = []
    for i in range(dim):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != dim:
                    print(f"❌ Error: Expected exactly {dim} values. Try again.")
                    continue
                a_rows.append(row)
                break
            except ValueError:
                print("❌ Error: Invalid numerical input. Try again.")

    print(f"\nEnter the {dim}x1 Constants Vector B (space-separated or line-by-line):")
    while True:
        try:
            b_input = input("Vector B: ").split()
            if len(b_input) != dim:
                print(f"❌ Error: Expected exactly {dim} values. Try again.")
                continue
            b_vec = np.array(b_input, dtype=float)
            break
        except ValueError:
            print("❌ Error: Invalid numerical input. Try again.")
            
    return np.array(a_rows), b_vec

def main():
    print("=" * 60)
    print("🚀 HIGH-PERFORMANCE N-DIMENSIONAL LINEAR SYSTEM SOLVER".center(60))
    print("=" * 60)

    # 1. Dynamic Dimension Selection
    try:
        dim = int(input("Enter system dimension N (e.g., 3 for a 3x3 matrix): "))
        if dim <= 0:
            raise ValueError
    except ValueError:
        print("❌ Critical Error: Dimension must be a positive integer.")
        sys.exit(1)

    # 2. Get inputs smoothly
    A, B = get_matrix_input(dim)

    # 3. Robust Numerical Solver with Error Handling
    print("\n" + "="*25 + " RESULTS " + "="*25)
    try:
        # Check conditioning before solving to prevent catastrophic cancellation errors
        if np.isclose(np.linalg.det(A), 0):
            print("❌ Error: Matrix A is singular (determinant is 0). System has no unique solution.")
            sys.exit(1)
            
        X = np.linalg.solve(A, B)
        print(f"✅ Solution Vector X: {X}")
        for idx, val in enumerate(X):
            print(f"   Variable x_{idx+1} = {val:.4f}")
            
    except np.linalg.LinAlgError:
        print("❌ Computation Error: Matrix is ill-conditioned or singular.")
        sys.exit(1)

    print("=" * 60)
    
    # 4. Optimized Vectorized Analytics
    print("📊 MATRIX METRICS & ANALYTICS")
    print(f"• Matrix Order : {A.shape[0]}x{A.shape[1]}")
    print(f"• Element Sum  : {np.sum(A)}")
    
    # Flattening and sorting efficiently (Fixes your variable naming bug)
    flat_sorted = np.sort(A, axis=None)
    print(f"• Sorted Array : {flat_sorted}")
    
    # Correct multi-dimensional flipping
    flipped_A = np.flip(A)
    print(f"• Flipped Matrix:\n{flipped_A}")
    print("=" * 60)

if __name__ == "__main__":
    main()