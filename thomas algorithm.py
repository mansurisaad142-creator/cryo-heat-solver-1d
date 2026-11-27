print("thomas algorithm")
MATRIX_A = list()
rows_A = int(input("Enter the number of rows for matrix A: "))
columns_A = int(input("Enter the number of columns for matrix A: "))
for i in range(rows_A):
    row = []
    for j in range(columns_A):
        row.append(float(input(f"Enter element [{i}][{j}]: ")))
    MATRIX.append(row)
print(MATRIX)

MATRIX_B = list()
rows_B = int(input("Enter the number of rows for matrix B: "))
columns_B = int(input("Enter the number of columns for matrix B: "))
for i in range(rows_B):
    row = []
    for j in range(columns_B):
        row.append(float(input(f"Enter element [{i}][{j}]: ")))
    MATRIX_B.append(row)
print(MATRIX_B)

print("thomas algorithm")
