import numpy as np

from io import StringIO

def gaussp(A, b):

    n = A.shape[0]

    for j in range(n - 1):

        p = j

        for i in range(j + 1, n):

            if abs(A[i][j]) > abs(A[j][j]):

                p = i

        A[[j, p]] = A[[p, j]]

        b[[j, p]] = b[[p, j]]

        for i in range(j + 1, n):

            mult = A[i][j] / A[j][j]

            for k in range(j + 1, n):

                A[i][k] = A[i][k] - mult * A[j][k]

            b[i] = b[i] - mult * b[j]

    x = np.copy(b)

    for i in range(n - 1, -1, -1):

        for j in range(i + 1, n):

            x[i] = x[i] - A[i][j] * x[j]

        x[i] = x[i] / A[i][i]

    return x

def main():

    A_in = """
            2 -2 -1

            4 1 -2

            -2 1 -1
                """

    b_in = """
            -2

            1

            -3
            """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    x = gaussp(A, b)

    print(A)

    print(b)

    print(x)

#main()
