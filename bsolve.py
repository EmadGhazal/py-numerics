import numpy as np

from io import StringIO

def bsolve(U, x):

    n = U.shape[0]

    for i in range(n - 1, -1, -1):

        for j in range(i + 1, n):

            x[i] = x[i] - U[i][j] * x[j]

        x[i] = x[i] / U[i][i]

    return x

def main():

    A_in = """
            2 1 0 0

            0 1 2 0

            0 0 -1 1

            0 0 0 1
                """

    b_in= """
            1

            1

            -2

            -1
            """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    b = b.reshape(b.shape[0], 1)

    x = bsolve(A, b)

    print(x)

#main()
