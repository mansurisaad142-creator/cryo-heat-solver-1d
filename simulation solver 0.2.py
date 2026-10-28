import numpy as np
import scipy as science
import math

print("=== PURE PYTHON FUNDAMENTAL MATRIX ENGINE ===")

rows1 = int(input(" enter row number: "))
cols1 = int(input(" enter column number : "))

# Step 1: Initialize an empty container for our matrix
# ek khali box liya matrix naam ka 
matrix_A = [ ]

print(f"\nEnter elements for a {rows1}x{cols1} matrix:")
# Step 2: Pure loop logic to capture row and column inputs
# I ke liye loop chalaya and row naam ke khali box print karwate 
for i in range(rows1):
    current_row = [ ]
    # j ka loop chalaya element naam ke ke liye user se input liye i+1 ,j+1 ke liye 
    for j in range(cols1):
        element = float(input(f"Enter element at Position [{i+1}][{j+1}]: "))
        # element ko row me append kar diya 
        current_row.append(element)
    # Append the completed row into our main matrix list
    # fir niche aaye and i wale loop and j wale loop ke bich me so that sab shuru se na ho jaye matrix me row append kar diya 
    matrix_A.append(current_row)
    
   
print("\n" + "="*40)
print("📊 RENDERED MATRIX OUTPUT (PURE VISUALIZATION)")
print("="*40)

# Step 3: Pure nested loop to print it like a grid
print ( " matrix A =")
# matrix me andar loop chalaya and formatted row naam ki definition banayi jisme bola ki 2f tak digit chahiye and also for every row 
for row1 in matrix_A:
    # Format each float value to 2 decimal places cleanly
   
    formatted_row = [f"{val:.4f}" for val in row1]
   # isme humne print me comma hatane ke liye direct space de ke .join formatted row ka use kiya hai 
    print(  "          " ,"[ " + "  ".join(formatted_row) +" ]")

print("="*40)

# Step 4: Extracting structural metrics without libraries
print(f"Total rows in matrix A ={(rows1)}")
print(f"Total cols in matrix A ={(cols1)}")
    
print ("=" * 50)
 
#=================================================================================================#

print ( " write B matrix  ")

rows2 = cols1
cols2 = int(input(" enter column number : "))

matrix_B= [ ]

print(f"\nEnter elements for a {rows2}x{cols2} matrix:")
# Step 2: Pure loop logic to capture row and column inputs
for i in range(rows2):
    current_row = [ ]
    for j in range(cols2):
        element = float(input(f"Enter element at Position [{i+1}][{j+1}]: "))
        current_row.append(element)
    # Append the completed row into our main matrix list
    matrix_B.append(current_row)

print("\n" + "="*40)
print("📊 RENDERED MATRIX OUTPUT (PURE VISUALIZATION)")
print("="*40)

# Step 3: Pure nested loop to print it like a grid
print( " matrix B = ")
for row2 in matrix_B:
    # Format each float value to 2 decimal places cleanly
    formatted_row = [f"{val:.2f}" for val in row2]
    
    print( "          " , "[ " + "  ".join(formatted_row) + " ]")

print("="*40)

# Step 4: Extracting structural metrics without libraries
print(f"Total rows in matrix B   = {(rows2)}")
print(f"Total cols in matrix B   = {(cols2)}")
         
print ("=" * 50)


#=================================================================================================#

#determinant_A=| matrix_A |