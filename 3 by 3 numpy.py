import numpy as np
print ('first matrix must be square')
A=np.array([[int(input("A[1][1]: ")),
             int(input("A[1][2]: ")),
             int(input("A[1][3]: "))],
             [int(input("A[2][1]: ")),
              int(input("A[2][2]: ")),
              int(input("A[2][3]: "))],
              [int(input("A[3][1]: ")),
               int(input("A[3][2]: ")),
               int(input("A[3][3]: "))]])

B=np.array([int(input("B[1][1]: ")),
            int(input("B[2][1]: ")),
            int(input("B[3][1]: "))])
print('determinant', np.linalg.det(A))
try:
    X=np.linalg.solve( A , B )
    print ('X=',X)
    print ("="*50)
    print ('X=',X[0])
    print ('Y=',X[1])
    print ('Z=',X[2])

except  np.linalg.LinAlgError:
    print(" matrix is singular : no solution exist")

