import numpy
import math

def getmatrixlu(a, b):

    lm = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    um = [[0 for i in range(len(a[0]))] for j in range(len(a))]


    #Diagonal elements of U are 1
    #The first elements of each column are equal
    for i in range(len(a)):
        lm[i][0] = a[i][0]
        um[i][i] = 1.0


    #The elements of the first line of the matrix U (U12, U13) are => A12/L11 and A13/L11
    for i in range(1, len(a)):
        um[0][i] = a[0][i] / lm[0][0]

    #The elements of the second column of L are given by: L22 = A22-L21*U12 and L32 = A32-L31*U12
    #The formula is: A[][] - Element behind * element on top

    for i in range(len(a)):
        for j in range(len(a[0])):
            if i >= j:
                sumatrix = [lm[i][z] * um[z][i] for z in range(j)]
                _sum = sum(sumatrix)
                lm[i][j] = a[i][j] - _sum
            else:
                um[i][j] = (a[i][j] - sum([lm[i][k] * um[k][j] for k in range(i)])) / lm[i][i]

    return lm, um


def k_method(a, b):
    l, u = getmatrixlu(a, b)
    y = numpy.linalg.inv(l).dot(b)  #Y = (L ^ -1) * B
    xm = numpy.linalg.inv(u).dot(y) #X = (U^-1) * Y
    return xm.tolist()


A = [[1, 1, 1], [3, -1, 2], [2, 0, 2]]
B = [8, -1, 5]
x = k_method(A, B)
print(x)



def formLU(A):
    L = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    U = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        L[i][0] = A[i][0]
        for j in range(len(A[0])):
            if(i >= j):
                L[i][j] = A[i][j] - sum([L[i][k]*U[k][j] for k in range(0,j)])
        U[0][i] = A[0][i] / L[0][0]
        for j in range(len(A[0])):
            if( i <= j):
                U[i][j] = (A[i][j] - sum([L[i][k]*U[k][j] for k in range(0,i)]))/L[i][i]
    return (L,U)

def solve_khalesky(S,L,U):
    X = [0,0,0]
    Y = [0,0,0]
    for i in range(len(Y)):
        Y[i] = (S[i] - sum([L[i][k]*Y[k] for k in range(len(S))]))/L[i][i]
    for i in range(len(X)-1,-1,-1):
        X[i] = (Y[i] - sum([U[i][k]*X[k] for k in range(len(Y))]))/U[i][i]

    return X

L,U = formLU(A)
X = solve_khalesky(B,L,U)
print(X)