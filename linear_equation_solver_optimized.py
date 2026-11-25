import math  # math module import kiya - math.fabs ke liye (absolute value)

# ============================================================
# MATRIX A INPUT FUNCTION
# User se coefficient matrix (A) ke input le rahe hain
# Gaussian elimination ke liye A matrix hona zaroori hai
# ============================================================
def Matrix_A_Input():
    MAX_ATTEMPTS = 5  # maximum 5 baar try karne ka chance - agar 5 baar galat toh stop
    attempts = 0  # attempt counter initialize kiya

    # ----- ROW NUMBER INPUT -----
    # row number input with error handling
    rows_A = 0  # rows_A variable initialize kiya with 0
    while attempts < MAX_ATTEMPTS:  # jab tak attempts 5 se kam hain loop chalao
        try:  # try block - error handle karne ke liye
            rows_A = int(input(" enter row number: "))  # user se input lo aur integer mein convert karo
            if rows_A > 0:  # agar row number 0 se bada hai toh valid hai
                break  # loop se bahar nikal jao
            print("Row number must be greater than 0")  # error message print karo
        except ValueError:  # agar error aaya toh yahan catch karo
           print("Please enter a valid number")  # user ko error message do
        attempts += 1  # attempt count mein 1 add karo (har iteration ke baad)
    if attempts >= MAX_ATTEMPTS:  # agar 5 baar try kar chuke hain
        print("Too many invalid attempts.")  # message print karo
        return None, None, None  # None return karo (error indicate karne ke liye)

    # ----- COLUMN NUMBER INPUT -----
    cols_A = 0  # cols_A variable initialize kiya with 0
    attempts = 0  # attempt counter reset kiya
    while attempts < MAX_ATTEMPTS:  # jab tak attempts 5 se kam hain loop chalao
        try:  # try block - error handle karne ke liye
            cols_A = int(input(" enter column number: "))  # user se input lo aur integer mein convert karo
            if cols_A > 0:  # agar column number 0 se bada hai toh valid hai
                break  # loop se bahar nikal jao
            print("Column number must be greater than 0")  # error message print karo
        except ValueError:  # agar error aaya toh yahan catch karo
            print("Please enter a valid number")  # user ko error message do
        attempts += 1  # attempt count mein 1 add karo
    if attempts >= MAX_ATTEMPTS:  # agar 5 baar try kar chuke hain
        print("Too many invalid attempts.")  # message print karo
        return None, None, None  # None return karo (error indicate karne ke liye)

    # ----- SQUARE MATRIX CHECK -----
    # Gaussian elimination ke liye matrix square hona chahiye (n x n)
    # Agar rows != cols toh unique solution nahi milega
    if rows_A != cols_A:  # agar rows aur cols equal nahi hain
        print("Matrix must be square (rows = columns)")  # user ko error message do
        return None, None, None  # None return karo (error indicate karne ke liye)

    # ----- MATRIX ELEMENTS INPUT -----
    matrix_A = []  # khali list banaya matrix store karne ke liye
    print(f"\nEnter elements for a {rows_A}x{cols_A} matrix:")  # user ko matrix size dikhaya
    for i in range(rows_A):  # har row ke liye loop - i = row index (0 se start)
        current_row = []  # temporary row banaya - current row ke elements store karne ke liye
        for j in range(cols_A):  # har column ke liye loop - j = column index (0 se start)
            attempts = 0  # attempt counter reset kiya
            while attempts < MAX_ATTEMPTS:  # jab tak attempts 5 se kam hain loop chalao
                try:  # try block - error handle karne ke liye
                    s = input(f" enter element [{i+1}][{j+1}]: ")  # element input lo (1-based display)
                    if s.strip() == "":  # agar input empty hai toh error
                        print("Input cannot be empty")  # error message print karo
                        attempts += 1  # attempt count increment karo
                        continue  # loop continue karo (input wapas lo)
                    current_row.append(float(s))  # string ko float mein convert karo aur row mein daalo
                    break  # loop se bahar nikal jao (valid input mil gaya)
                except ValueError:  # agar float conversion fail ho gaya
                    print("Please enter a valid number")  # error message print karo
                    attempts += 1  # attempt count increment karo
            if attempts >= MAX_ATTEMPTS:  # agar 5 baar try kar chuke hain
                print("Too many invalid attempts.")  # message print karo
                return None, None, None  # None return karo (error indicate karne ke liye)
        matrix_A.append(current_row)  # current row ko main matrix mein daalo

    return matrix_A, rows_A, cols_A  # matrix aur dimensions return karo


# ============================================================
# MATRIX B INPUT FUNCTION
# User se constant matrix (B) ke input le rahe hain
# B matrix = RHS (right-hand side) constants
# rows_B = rows_A (matrix multiplication rule)
# ============================================================
def Matrix_B(rows_A):
    print("so row of b = ", rows_A)  # user ko dikhaya B ke rows = A ke rows
    rows_B = rows_A  # B matrix ka row count set kiya - A ke rows ke barabar
    MAX_ATTEMPTS = 5  # maximum 5 baar try karne ka chance

    # ----- COLUMN NUMBER INPUT -----
    attempts = 0  # attempt counter initialize kiya
    while attempts < MAX_ATTEMPTS:  # jab tak attempts 5 se kam hain loop chalao
        try:  # try block - error handle karne ke liye
            cols_B = int(input(" enter column number: "))  # user se input lo aur integer mein convert karo
            if cols_B > 0:  # agar column number 0 se bada hai toh valid hai
                break  # loop se bahar nikal jao
            print("Column number must be greater than 0")  # error message print karo
        except ValueError:  # agar error aaya toh yahan catch karo
            print("Please enter a valid number")  # error message print karo
        attempts += 1  # attempt count mein 1 add karo
    if attempts >= MAX_ATTEMPTS:  # agar 5 baar try kar chuke hain
        print("Too many invalid attempts.")  # message print karo
        return None, None, None  # None return karo (error indicate karne ke liye)

    # ----- MATRIX ELEMENTS INPUT -----
    matrix_B = []  # khali list banaya B matrix store karne ke liye
    print(f"\nEnter elements for a {rows_B}x{cols_B} matrix:")  # user ko matrix size dikhaya
    for i in range(rows_B):  # har row ke liye loop - i = row index (0 se start)
        current_row = []  # temporary row banaya - current row ke elements store karne ke liye
        for j in range(cols_B):  # har column ke liye loop - j = column index (0 se start)
            attempts = 0  # attempt counter reset kiya
            while attempts < MAX_ATTEMPTS:  # jab tak attempts 5 se kam hain loop chalao
                try:  # try block - error handle karne ke liye
                    s = input(f"Enter element at Position [{i+1}][{j+1}]: ")  # element input lo (1-based display)
                    if s.strip() == "":  # agar input empty hai toh error
                        print("input cannot be empty")  # error message print karo
                        attempts += 1  # attempt count increment karo
                        continue  # loop continue karo (input wapas lo)
                    current_row.append(float(s))  # string ko float mein convert karo aur row mein daalo
                    break  # loop se bahar nikal jao (valid input mil gaya)
                except ValueError:  # agar float conversion fail ho gaya
                    print("input cannot be string")  # error message print karo
                    attempts += 1  # attempt count increment karo
            if attempts >= MAX_ATTEMPTS:  # agar 5 baar try kar chuke hain
                print("Too many invalid attempts.")  # message print karo
                return None, None, None  # None return karo (error indicate karne ke liye)
        matrix_B.append(current_row)  # current row ko main matrix mein daalo
    return matrix_B, rows_B, cols_B  # matrix aur dimensions return karo


# ============================================================
# AUGMENT MATRIX FUNCTION
# A aur B ko combine karke augmented matrix banate hain
# Augmented matrix = [A | B] - har row mein A ke elements ke sath B ke elements jod diye
# Example: A = [[1,2],[3,4]], B = [[5],[6]] → AUG = [[1,2,5],[3,4,6]]
# ============================================================
def augment_matrix(matrix_A, matrix_B, rows_A):
    # har row mein A aur B ko jod do using list comprehension
    # matrix_A[i] = i-th row of A, matrix_B[i] = i-th row of B
    # + operator se dono lists combine ho jati hain
    return [matrix_A[i] + matrix_B[i] for i in range(rows_A)]  # augmented matrix return karo


# ============================================================
# ELIMINATION PROCESS FUNCTION
# Forward elimination with partial pivoting - upper triangular form banate hain
# Upper triangular = diagonal ke neeche sab elements zero
# Partial pivoting = current column mein sabse bada element ko pivot banate hain
# Ye numerical stability ke liye important hai - floating-point errors kam hoti hain
# ============================================================
def elimination_process(AUG):
    rows_AUG = len(AUG)  # total rows count nikala
    cols_AUG = len(AUG[0])  # total columns count nikala

    # ----- TOLERANCE CALCULATION -----
    # Tolerance ye check karne ke liye hai ki element effectively zero hai ya nahi
    # Floating-point arithmetic mein exact zero kabhi nahi milta, isliye tolerance use karte hain
    max_value = max(abs(AUG[i][j]) for i in range(rows_AUG) for j in range(rows_AUG))  # matrix mein sabse bada element dhundho
    TOL = 1e-12 * max(max_value, 1.0)  # 1e-12 = very small number, tolerance set kiya (relative to max value)

    for i in range(rows_AUG):  # har row ke liye loop - i = current row index
        # ----- PARTIAL PIVOTING -----
        # Current column (i-th column) mein sabse bada element dhundho
        # Pivot = diagonal element - jo row ko eliminate karega
        pivot_row = i  # initially assume current row hi pivot hai
        pivot_value = abs(AUG[i][i])  # current pivot ka absolute value
        for k in range(i + 1, rows_AUG):  # rows below current row check karo
            if abs(AUG[k][i]) > pivot_value:  # agar k-th row mein bada element mila
                pivot_value = abs(AUG[k][i])  # pivot value update karo
                pivot_row = k  # pivot row update karo

        # ----- SINGULAR MATRIX CHECK -----
        # Agar pivot bahut chhota hai toh matrix singular hai (no unique solution)
        if pivot_value < TOL:  # agar pivot value tolerance se kam hai
            raise ValueError(f"Matrix is singular (column {i})")  # error raise karo

        # ----- ROW SWAPPING -----
        # Agar pivot row current row se alag hai toh swap karo
        if pivot_row != i:  # agar pivot row change hua
            AUG[i], AUG[pivot_row] = AUG[pivot_row], AUG[i]  # rows swap kar do

        DIAGONAL = AUG[i][i]  # diagonal element (pivot) store kiya for later use

        # ----- ELIMINATION - ROWS BELOW KO ZERO BANAO -----
        # Ab rows below current row ko eliminate karte hain
        for H in range(i + 1, rows_AUG):  # H = row index (current row ke neeche)
            factor = AUG[H][i] / DIAGONAL  # elimination factor calculate karo
            # Factor = H-th row mein i-th column ko zero banane ke liye multiplier
            # for example: for factor of 2nd row 1st column element
            # factor = AUG[1][0] / AUG[0][0]
            # means factor = (element below pivot) / (pivot element) column wise
            # for example: for factor of 3rd row 2nd column element
            # factor = AUG[2][1] / AUG[1][1]
            for j in range(cols_AUG):  # har column ke liye loop
                # here AUG[H][j] vo position wala element hai jisko eliminate karna hai
                # and row[i][j] purana wala element jo factor se multiply hoke eliminate karega 
                AUG[H][j] = AUG[H][j] - factor * AUG[i][j]  # eliminate karo
                # Formula: new_value = old_value - factor * pivot_row_value
                # Isse H-th row mein i-th column zero ho jata hai
                # yaha pe humne bola lets say aug[1][0] = 4 and factor = 2 so and we want to make aug[1][0] = 0 & aug[0][0] = 2
                # so 4 - 2 * 2 = 0
                # for example: for elimination of 2nd row 1st column element
                # AUG[1][0] = AUG[1][0] - factor * AUG[0][0]

    return AUG  # upper triangular matrix return karo


# ============================================================
# BACK SUBSTITUTION FUNCTION
# Upper triangular matrix se solution nikalte hain
# Last row se start karte hain kyunki wahan sabse kam unknown variables hote hain
# Phir gradually upar jaate hain - har row mein pehle se solve kiye variables ko substitute karte hain
# ============================================================
def back_substitution(AUG, cols_B):
    rows_AUG = len(AUG)  # total rows count nikala
    X_VECTORS = [[0.0] * cols_B for _ in range(rows_AUG)]  # solution matrix banaya - sabse pehle zeros initialize kiye
    # X_VECTORS = [[0,0,...], [0,0,...], ...] - har row ke liye cols_B columns

    max_val = max(abs(AUG[i][i]) for i in range(rows_AUG))  # diagonal mein sabse bada element dhundho
    TOL = 1e-12 * max(max_val, 1.0)  # tolerance set kiya (singular check ke liye)

    for b_col in range(cols_B):  # har B column ke liye loop (multiple RHS support)
        # loop chalaya for b column - har column alag equation system represent karta hai
        rhs_col = rows_AUG + b_col  # RHS column ka index calculate kiya

        # Augmented matrix mein last cols_B columns RHS hote hain
        for i in reversed(range(rows_AUG)):  # ulta loop - last row se first row tak
            # reversed(range(n)) = [n-1, n-2, ..., 0]
            RHS = AUG[i][rhs_col]  # RHS value lo - augmented matrix ke last column se | B wala 
            for j in range(i + 1, rows_AUG):  # pehle se solve kiye variables ke terms
                # Diagonal ke right side wale columns - jo already solve ho chuke hain
                # ab yaha pe ye loop chalaya hai to substract previous calculated values
                # yaha loop i + 1 se start karte hai because diogonal ke niche wale elements already zero hote hai upper triangular form mein
                # and diogonal ke help se hi hum solution nikalte hai
                # so hum diagonal ke baad wale element pe loop chalate hai
                # value lete hai X_VECTORS[j] jo already calculate kiye gaye hai
                RHS = RHS - AUG[i][j] * X_VECTORS[j][b_col]  # known terms ko equation se hatao
                # Formula: new_RHS = old_RHS - coefficient * known_value
                # Ye substitution hai - known variables ko equation se remove karte hain
                # yaha humne |B me se pehle se calculate kiye gaye X values ko uske assigned value se multiply karke subtract kar diya
                # AUG[i][j] is the coefficient of X[i] in the equation jispe hum work kar rahe hai
                # X_VECTORS[j][b_col] is the value of X[j] for this B column jo already calculate kiya gaya hai
                # for example: 5X + 3Y = 10 me humne Y already calculate kiya hai to hum unhe multiply karke subtract karte hai
                # for example: 2X + 3Y = 10 me humne Y already calculate kiya hai to hum unhe multiply karke subtract karte hai
                # so yaha 2x 0 ho gya to sirf 3y hi reh jayega and y ki value humne already calculate hai
                # ab hum work kar rahe hai on 5x + 3y = 10 me x ki value nikalne ke liye so yaha aug[i][j] 3 hoga and X_VECTORS[j][b_col] y ki value hoga
        

            if abs(AUG[i][i]) < TOL:  # diagonal check - agar zero ke bahut qareeb hai
                raise ValueError(f"Singular at row {i}")  # error raise karo

            X_VECTORS[i][b_col] = RHS / AUG[i][i]  # divide karo variable isolate karne ke liye
            # Formula: variable = RHS / diagonal_coefficient
            # Isse current variable ki value mil jati hai
            # fr humne remaining sum ko diagonal se divide kar diya to humne x ki value nikal li

    return X_VECTORS  # solution matrix return karo


# ============================================================
# PRINT SOLUTION FUNCTION
# Solution matrix ko clean format mein print karte hain
# Har variable ki value display karte hain
# ============================================================
def print_final_solution(X_VECTORS):
    print("\nFINAL SOLUTION:")  # header print karo
    rows = len(X_VECTORS)  # total rows count nikala
    cols = len(X_VECTORS[0]) if rows > 0 else 0  # total columns count nikala (empty check)
    for i in range(rows):  # har row ke liye loop - i = row index
        for j in range(cols):  # har column ke liye loop - j = column index
            print(f"X[{i}][{j}] = {X_VECTORS[i][j]}")  # value print karo with index


# ============================================================
# ERROR CHECK FUNCTION
# Solution ko verify karte hain - AX = B mein X ko daalke check karte hain
# Residual error = |A*X - B| - ye chhota hona chahiye agar solution sahi hai
# Agar error bahut bada hai toh solution galat hai
# ============================================================
def ERROR_CHECK(matrix_A, X_VECTORS, matrix_B):
    # yaha hum error check karte hai
    max_error = 0.0  # maximum error store karne ke liye - initially 0
    for i in range(len(matrix_A)):  # pehle row ke liye - i = row index of A
        for j in range(len(X_VECTORS[0])):  # phir column ke liye - j = column index of X
            calculated_value = 0.0  # A*X calculate karne ke liye - initially 0
            for k in range(len(X_VECTORS)):  # phir uske andar ke elements ke liye - k = common dimension
                # Formula: (A*X)[i][j] = sum(A[i][k] * X[k][j]) for all k
                calculated_value += matrix_A[i][k] * X_VECTORS[k][j]  # matrix_A[i][k] * X_VECTORS[k][j] ka result calculated_value me add ho jayega
            error = math.fabs(calculated_value - matrix_B[i][j])  # absolute error nikalo
            # Error = |calculated - actual| - absolute value using math.fabs
            max_error = max(max_error, error)  # maximum error update karo
    print(f"\nMax residual error = {max_error:.3e}")  # error print karo (scientific notation)
    # .3e = 3 decimal places in scientific notation (e.g., 1.234e-10)
    return max_error  # maximum error return karo


# ============================================================
# MAIN FUNCTION
# Complete Gaussian elimination flow execute karte hain
# Steps: Input → Augment → Eliminate → Back Substitute → Print → Verify
# ============================================================
def main():
    #================================================================================
    #================================================================================
    #================================================================================
    # Gaussian Elimination
    print("Ax = B")  # system dikhaya - linear equation system
    print("Where A is the coefficient matrix, x is the variable matrix, and B is the constant matrix")

    # ----- STEP 1: MATRIX A INPUT -----
    matrix_A, rows_A, cols_A = Matrix_A_Input()  # user se A matrix lo (coefficient matrix)
    if matrix_A is None:  # agar input fail ho gaya (None returned)
        print("\nERROR: Failed to create Matrix A.")
        return

    # ----- STEP 2: MATRIX B INPUT -----
    matrix_B, rows_B, cols_B = Matrix_B(rows_A)  # user se B matrix lo (constant matrix)
    # rows_A pass kiya kyunki B ke rows = A ke rows hote hain
    if matrix_B is None:  # agar input fail ho gaya (None returned)
        print("\nERROR: Failed to create Matrix B.")
        return

    # ----- STEP 3: AUGMENTED MATRIX BANAO -----
    AUG = augment_matrix(matrix_A, matrix_B, rows_A)  # A aur B ko combine karo
    # Augmented matrix = [A | B] - har row mein A aur B ko jod diya

    # ----- STEP 4: FORWARD ELIMINATION -----
    print("ELIMINATION PROCESS")
    print("=" * 50)
    AUG = elimination_process(AUG)  # upper triangular form banao
    # Elimination process = partial pivoting + row operations
    # Result: diagonal ke neeche sab elements zero

    # ----- STEP 5: BACK SUBSTITUTION -----
    X_VECTORS = back_substitution(AUG, cols_B)  # solution nikalo
    # Back substitution = last row se start karke variables calculate karna

    # ----- STEP 6: SOLUTION PRINT KARO -----
    print_final_solution(X_VECTORS)  # display karo
    # Har variable ki value clean format mein print hoti hai

    # ----- STEP 7: ERROR CHECK -----
    ERROR_CHECK(matrix_A, X_VECTORS, matrix_B)  # verify karo
    # Residual error check karte hain - AX = B verify karte hain


if __name__ == "__main__":
    main()