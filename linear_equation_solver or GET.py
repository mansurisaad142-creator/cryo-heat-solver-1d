import math

def Matrix_A():
    # Matrix A input lene ka function
    MAX_ATTEMPTS = 5
    attempts = 0

    # row number input with error handling
    while attempts < MAX_ATTEMPTS:
        try:
            rows_A = int(input(" enter row number: "))
            if rows_A> 0:
                break
            print("ERROR: Row number must be greater than 0")
        except ValueError:
            print("ERROR: Please enter a valid number")
        attempts += 1
    if attempts >= MAX_ATTEMPTS:
        print("ERROR: Too many invalid attempts. Exiting.")
        return None, None, None

    attempts = 0
    # column number input with error handling
    while attempts < MAX_ATTEMPTS:
        try:
            cols_A = int(input(" enter column number : "))
            if cols_A > 0:
                break
            print("ERROR: Column number must be greater than 0")
        except ValueError:
            print("ERROR: Please enter a valid number")
        attempts += 1
    if attempts >= MAX_ATTEMPTS:
        print("ERROR: Too many invalid attempts. Exiting.")
        return None, None, None

    attempts = 0
    # ensure matrix is square
    while attempts < MAX_ATTEMPTS:
        try:
            if rows_A == cols_A:
                break
            print("Matrix must be square (rows = columns)")
            cols_A = int(input(" enter column number again : "))
        except ValueError:
            print("ERROR: Please enter a valid number")
        attempts += 1
    if attempts >= MAX_ATTEMPTS:
        print("ERROR: Too many invalid attempts. Exiting.")
        return None, None, None

    matrix_A = [ ]  # ek khali list banayi matrix ko store karne ke liye
    print(f"\nEnter elements for a {rows_A}x{cols_A} matrix:")  # user ko bataya kitne elements daalne hain

    # row ke liye loop chalaya - i = row index
    for mat_A_row in range(rows_A):
        current_row = [ ]  # har row ke liye ek temporary list banayi
        # column ke liye loop chalaya - j = column index
        for mat_A_col in range(cols_A):
            # element input with error handling - keep asking until valid input
            attempts = 0
            while attempts < MAX_ATTEMPTS:
                try:
                    element_input = input(f"Enter element at Position [{mat_A_row+1}][{mat_A_col+1}]: ")
                    if element_input.strip() == "":
                        print("ERROR: Input cannot be empty, please enter a number")
                        attempts += 1
                        continue
                    element = float(element_input)
                    break
                except ValueError:
                    print("ERROR: Please enter a valid number")
                    attempts += 1
            if attempts >= MAX_ATTEMPTS:
                print("ERROR: Too many invalid attempts. Exiting.")
                return None, None, None
            current_row.append(element)  # element ko current row mein daal diya
        matrix_A.append(current_row)  # current row ko main matrix mein daal diya
    return matrix_A, rows_A, cols_A  # matrix + dimensions return kar diya

def Matrix_B(rows_A):
    # Matrix B input lene ka function - rows_A ko input liya kyunki A ke rows = B ke rows
    print(" write B matrix  ")  # B matrix likhne ko bola
    print(" IN {KU}=X TYPE SYSTEM ")  # system type bataya
    print("NUMBER OF ROWS OF A IS EQUAL TO NUMBER OF ROW OF B")  # matrix multiplication rule
    print("so row of b = ", rows_A)  # B ke rows = A ke rows
    rows_B= rows_A  # B ke rows = A ke rows

    MAX_ATTEMPTS = 5
    attempts = 0

    # column number input with error handling
    while attempts < MAX_ATTEMPTS:
        try:
            cols_B = int(input(" enter column number : "))
            if cols_B > 0:
                break
            print("ERROR: Column number must be greater than 0")
        except ValueError:
            print("ERROR: Please enter a valid number")
        attempts += 1
    if attempts >= MAX_ATTEMPTS:
        print("ERROR: Too many invalid attempts. Exiting.")
        return None, None, None

    matrix_B = [ ]  # khali list banayi B matrix ke liye
    print(f"\nEnter elements for a {rows_B}x{cols_B} matrix:")  # user ko bataya kitne elements

    # row loop
    for mat_b_row in range(rows_B):
        current_row = [ ]  # temporary row
        # column loop
        for mat_b_col in range(cols_B):
            # element input with error handling - keep asking until valid input
            attempts = 0
            while attempts < MAX_ATTEMPTS:
                try:
                    element_input = input(f"Enter element at Position [{mat_b_row+1}][{mat_b_col+1}]: ")
                    if element_input.strip() == "":
                        print("ERROR: Input cannot be empty, please enter a number")
                        attempts += 1
                        continue
                    element = float(element_input)
                    break
                except ValueError:
                    print("ERROR: Please enter a valid number")
                    attempts += 1
            if attempts >= MAX_ATTEMPTS:
                print("ERROR: Too many invalid attempts. Exiting.")
                return None, None, None
            current_row.append(element)  # row mein daalo
        matrix_B.append(current_row)  # main matrix mein daalo
    return matrix_B, rows_B, cols_B  # matrix + dimensions return

def create_matrix_X(rows_X, cols_X):
    # Matrix X display karne ka function - ye sirf dikhata hai solve nahi karta
    matrix_X = [ ]  # khali list
    # loop chalaya X matrix ke liye
    for mat_x_row in range(rows_X):
        current_row = []  # temporary row
        for mat_x_col in range(cols_X):
            # X ke elements print kiye - sirf display ke liye strings use kiye
            var_name = f"X[{mat_x_row}][{mat_x_col}]"
            print(var_name)
            current_row.append(var_name)  # string add kiya
        matrix_X.append(current_row)  # row mein daala
    return matrix_X  # X matrix return kiya

def print_matrices(matrix_A, rows_A, cols_A, matrix_B, rows_B, cols_B, matrix_X):
    # Matrix A print kiya
    print("\n" + "="*40)  # separator line
    print(f"\nA ({rows_A}x{cols_A})  *  X ({cols_A}x{cols_B})  =  B ({rows_A}x{cols_B})\n")  # equation dikhaya

    print("Matrix A =")
    for temperory_row in matrix_A:
        # har element ko 3 decimal tak format kiya
        formatted_row = [f"{val:.3f}" for val in temperory_row]
        # brackets mein space separated print kiya
        print("          " + "[ " + "  ".join(formatted_row) + " ]")

    print("=" * 50)  # separator

    # Matrix X print kiya
    print("Matrix X (variable names) =")
    for temperorary_row_x in matrix_X:
        formatted_row = [f"{val}" for val in temperorary_row_x]  # strings directly liye
        print("          " + "[ " + "  ".join(formatted_row) + " ]")

    print("=" * 50)  # separator

    # Matrix B print kiya
    print("Matrix B =")
    for temperory_row_b in matrix_B:
        formatted_row = [f"{val:.2f}" for val in temperory_row_b]  # 2 decimal tak format
        print("          " + "[ " + "  ".join(formatted_row) + " ]")

    print("=" * 50)  # separator

def order_of_matrices(rows_A, cols_A, cols_B):
    # Augmented matrix [A | B] banaya - A aur B ko row-wise combine kiya
    print(f"matrix_A  order is {rows_A} x {cols_A}")
    print(f"matrix_x   order is {cols_A}  x {cols_B} ")
    print(f"matrix_B  order is {rows_A} x {cols_B}")

    print(f"\nAugmented Matrix [ X = A | B] showing complete equation:")
    print("=" * 70)

def print_proper_augmented_matrix(matrix_X, matrix_A, matrix_B, rows_A, cols_B):
    for i in range(rows_A):
        # X part - variables like X[0][0], X[0][1], etc.
        x_part = matrix_X[i][:cols_B]  # Take only cols_B elements
        # A part - coefficients from matrix A
        a_part = [f"{val:.3f}" for val in matrix_A[i]]
        # B part - constants from matrix B
        b_part = [f"{val:.3f}" for val in matrix_B[i]]
        # Combine to show: X = A | B
        formatted_row = "  ".join(x_part) + "  =  " + "  ".join(a_part) + "  |  " + "  ".join(b_part)
        print("  " + formatted_row)

def print_augmented_matrix_with_solution(matrix_A, matrix_B, X_VECTORS, rows_A, cols_B):
    print("\n" + "=" * 70)
    print("AUGMENTED MATRIX WITH SOLUTION VALUES:")
    print("=" * 70)
    for i in range(rows_A):
        # X part - actual solution values (row of X_VECTORS)
        x_part = []
        for j in range(cols_B):
            x_part.append(f"{X_VECTORS[i][j]:.3f}")
        # A part - coefficients from matrix A
        a_part = [f"{val:.3f}" for val in matrix_A[i]]
        # B part - constants from matrix B
        b_part = [f"{val:.3f}" for val in matrix_B[i]]
        # Combine to show: X = A | B with actual values
        formatted_row = "  ".join(x_part) + "  =  " + "  ".join(a_part) + "  |  " + "  ".join(b_part)
        print("  " + formatted_row)
    print("=" * 70)

def augment_matrix(matrix_A, matrix_B, rows_A):
    AUG = [matrix_A[i] + matrix_B[i] for i in range(rows_A)]
    print("AUG=" , AUG)
    return AUG




def elimination_process(AUG):
    print("ELIMINATION PROCESS")
    print("=" * 50)

    rows_AUG = len(AUG)
    cols_AUG = len(AUG[0])

    for i in range(len(AUG)):  # har row ke liye loop - i = current row number
        # pehle check karo diagonal element non-zero hai ya nahi
        if abs(AUG[i][i]) >= 1e-15:  # agar diagonal element non-zero hai
            print("pivot is non-zero")  # message print karo
            DIAGONAL = AUG[i][i]  # DIAGONAL value set karo
        else:  # agar diagonal element zero hai toh swap karna padega
            print("pivot is zero")  # message print karo
            print("we need to swap rows")  # rows swap karne ki zarurat hai

            # ab rows ke neeche dekho non-zero element dhundne ke liye
            swapped = False
            for k in range(i + 1, rows_AUG):  # k = rows below current row (i+1 se start)
                if abs(AUG[k][i]) >= 1e-15:  # agar k-th row mein non-zero element mila
                    AUG[i], AUG[k] = AUG[k], AUG[i]  # rows swap kar do (i aur k exchange)
                    print(f" we swapped row {i} with row {k}")  # swap ka message print karo
                    DIAGONAL = AUG[i][i]  # DIAGONAL recalculate karo after swap
                    swapped = True
                    break  # loop stop karo, swap ho gaya

            if not swapped:  # agar loop poora chala aur koi non-zero nahi mila
                print("No non-zero pivot/diagonal element found, matrix is singular")  # matrix singular hai
                return None  # singular matrix, return None

        # DIAGONAL check karo before division
        if abs(DIAGONAL) < 1e-15:
            print(f"ERROR: Diagonal element at position {i} is too small ({DIAGONAL}). Matrix is singular.")
            return None

        # elimination loop - sab rows below pivot ko zero banao
        for H in range(i + 1, rows_AUG):  # H = rows below current pivot
            factor = AUG[H][i] / DIAGONAL  # factor calculate karo
            # for example: for factor of 2nd row 1st column element
            # factor = AUG[1][0] / AUG[0][0]
            # means factor = (element below pivot) / (pivot element) column wise
            # for example: for factor of 3rd row 2nd column element
            # factor = AUG[2][1] / AUG[1][1]
            print(f"factor for row {H} = {factor}")  # factor print karo
            for j in range(cols_AUG):  # har column ke liye
                AUG[H][j] = AUG[H][j] - factor * AUG[i][j]  # elimination
                # yaha pe humne bola lets say aug[1][0] = 4 and factor = 2 so and we want to make aug[1][0] = 0 & aug[0][0] = 2
                # so 4 - 2 * 2 = 0
                # for example: for elimination of 2nd row 1st column element
                # AUG[1][0] = AUG[1][0] - factor * AUG[0][0]
            print(f"Updated row {H} = {AUG[H]}")  # updated row print karo
            print("AUG = ", AUG)

    return AUG


def back_substitution(AUG, cols_B):
    print("\n" + "=" * 50)
    print("BACK SUBSTITUTION")
    print("=" * 50)

    rows_AUG = len(AUG)
    # cols_AUG = len(AUG[0])  # Not used, but kept for reference

    # X_VECTORS will be 2D array: rows_AUG x cols_B
    X_VECTORS = [[0] * cols_B for _ in range(rows_AUG)]

    # For each column in B (each right-hand side)
    for b_col in range(cols_B):
        rhs_col = rows_AUG + b_col  # Position of this B column in AUG
        print(f"\nSolving for B column {b_col + 1}:")

        for i in reversed(range(rows_AUG)):  # ulta loop - last row se shuru, first row tak
            sum = AUG[i][rhs_col]  # equation ka RHS (constant term) lo
            # yaha ek fallacy hai total coulmn 4 hote hai and -1 karte hi 3 position pe jana hota hai and calculation
            # se dekhe to ye column_aug -1 is nothing but | B column hota hai calculation se dekh sakte hai
            for j in range(i + 1, rows_AUG):  # pehle se solve kiye variables ke terms
                # ab yaha pe ye loop chalaya hai to substract previous calculated values
                # yaha loop i + 1 se start karte hai because diogonal ke niche wale elements already zero hote hai upper triangular form mein
                # and diogonal ke help se hi hum solution nikalte hai
                # so hum diagonal ke baad wale element pe loop chalate hai
                # value lete hai X_VECTORS[j] jo already calculate kiye gaye hai
                sum = sum - AUG[i][j] * X_VECTORS[j][b_col]  # known terms ko equation se hatao
                # yaha humne |B me se pehle se calculate kiye gaye X values ko uske assigned value se multiply karke subtract kar diya
                #  AUG[i][j] is the coefficient of X[i] in the equation jispe hum work kar rahe hai
                #  X_VECTORS[j][b_col] is the value of X[j] for this B column jo already calculate kiya gaya hai
                # for example: 5X + 3Y = 10 me humne Y already calculate kiya hai to hum unhe multiply karke subtract karte hai
                # for example: 2X + 3Y = 10 me humne Y already calculate kiya hai to hum unhe multiply karke subtract karte hai
                # so yaha 2x 0 ho gya to sirf 3y hi reh jayega and y ki value humne already calculate ki hai
                # ab hum work kar rahe hai on 5x + 3y = 10 me x ki value nikalne ke liye so yaha aug[i][j] 3 hoga and X_VECTORS[j][b_col] y ki value hoga

            # Check diagonal element before division
            if abs(AUG[i][i]) < 1e-15:
                print(f"ERROR: Diagonal element at position {i} is too small ({AUG[i][i]}). Matrix is singular.")
                return None

            X_VECTORS[i][b_col] = sum / AUG[i][i]  # remaining sum ko diagonal se divide karo
            # fr humne remaining sum ko diagonal se divide kar diya to humne x ki value nikal li

            print(f"X[{i}][{b_col}] = {X_VECTORS[i][b_col]}")  # solution print karo

    return X_VECTORS

def print_final_solution(X_VECTORS):
    print("\n" + "=" * 50)
    print("FINAL SOLUTION:")
    print("=" * 50)
    rows = len(X_VECTORS)
    cols = len(X_VECTORS[0]) if rows > 0 else 0

    for i in range(rows):  # har row ke liye
        for j in range(cols):  # har column ke liye
            print(f"X[{i}][{j}] = {X_VECTORS[i][j]}")


def  ERROR_CHECK(matrix_A, X_VECTORS, matrix_B): # yaha hum error check karte hai

    
    for i in range(len(matrix_A)): # pehle row ke liye
        for j in range(len(X_VECTORS[0])): # phir column ke liye
            calculated_value = 0
            for k in range(len(X_VECTORS)): # phir uske andar ke elements ke liye
                calculated_value += matrix_A[i][k] * X_VECTORS[k][j] # matrix_A[i][k] * X_VECTORS[k][j] ka result calculated_value me add ho jayega
                print(f"calculated_value[{i}][{j}] = {calculated_value}") # calculated_value print karo
                error = math.fabs(calculated_value - matrix_B[i][j]) # error calculate karo
                print(f"error[{i}][{j}] = {error} | calculated_value[{i}][{j}] = {calculated_value} | matrix_B[{i}][{j}] = {matrix_B[i][j]} ") # error print karo

    

def main():
    #================================================================================
    #================================================================================
    #================================================================================
    # Gaussian Elimination

    print("AUGMENTED MATRIX PRESENTATION ")
    print("=" * 50)

    print("Ax = B")
    print("Where A is the coefficient matrix, x is the variable matrix, and B is the constant matrix")

    # Step 1: Get Matrix A
    matrix_A, rows_A, cols_A = Matrix_A()
    if matrix_A is None:
        print("\nERROR: Failed to create Matrix A.")
        return

    # Step 2: Get Matrix B
    matrix_B, rows_B, cols_B = Matrix_B(rows_A)
    if matrix_B is None:
        print("\nERROR: Failed to create Matrix B.")
        return

    # Step 3: Create Matrix X for display
    matrix_X = create_matrix_X(cols_A, cols_B)

    # Step 4: Print all matrices
    print_matrices(matrix_A, rows_A, cols_A, matrix_B, rows_B, cols_B, matrix_X)

    # Step 5: Print order of matrices
    order_of_matrices(rows_A, cols_A, cols_B)

    # Step 6: Print proper augmented matrix with variables (before solving)
    print_proper_augmented_matrix(matrix_X, matrix_A, matrix_B, rows_A, cols_B)

    # Step 7: Create augmented matrix
    AUG = augment_matrix(matrix_A, matrix_B, rows_A)

    # Step 8: Run elimination process
    AUG = elimination_process(AUG)
    if AUG is None:
        print("\nERROR: Elimination process failed. Matrix is singular.")
        return

    # Step 9: Run back substitution
    X_VECTORS = back_substitution(AUG, cols_B)
    if X_VECTORS is None:
        print("\nERROR: Back substitution failed. Matrix is singular.")
        return

    # Step 10: Print augmented matrix with actual solution values (after solving)
    print_augmented_matrix_with_solution(matrix_A, matrix_B, X_VECTORS, rows_A, cols_B)

    # Step 11: Print final solution
    print_final_solution(X_VECTORS)
    
    # Step 12: Check error
    ERROR_CHECK(matrix_A, X_VECTORS, matrix_B)
    

if __name__ == "__main__":
    main()

