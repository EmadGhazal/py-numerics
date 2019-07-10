import numpy as np

from io import StringIO

def lup(A, b):

    n = A.shape[0]

    L = np.identity(n)

    P = np.identity(n)

    for j in range(n - 1):

        p = j

        for i in range(j + 1, n):

            if abs(A[i][j]) > abs(A[p][j]):

                p = i

        if p != j:

            A[[j, p]] = A[[p, j]]

            P[[j, p]] = P[[p, j]]

        for i in range(j + 1, n):

            mult = A[i][j] / A[j][j]

            A[i][j] = mult

            for k in range(j + 1, n):

                A[i][k] = A[i][k] - mult * A[j][k]

    U = np.triu(A)

    L = np.tril(A)

    np.fill_diagonal(L, 1.0)

    x = np.copy(b)

    x = np.matmul(P, x)

    for i in range(0, n):

        for j in range(0, i):

            x[i] = x[i] - L[i][j] * x[j]

        x[i] = x[i] / L[i][i]

    for i in range(n - 1, -1, -1):

        for j in range(i + 1, n):

            x[i] = x[i] - U[i][j] * x[j]

        x[i] = x[i] / U[i][i]

#    return """P, L, U,""" x

    return x

"""A_in = 
        0 1 0

        1 0 2

        -2 1 0
            

b_in= 
        0

        0

        0
        

A = np.genfromtxt(StringIO(unicode(A_in)), delimiter = " ")

b = np.genfromtxt(StringIO(unicode(b_in)), delimiter = " ")

P, L, U, x = lup(A, b)

print P, "\n"

print L, "\n"

print U, "\n"

print x
"""
