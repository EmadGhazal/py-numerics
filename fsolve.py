import numpy as np

from io import StringIO

def fsolve(L, x):

    n = L.shape[0]

    for i in range(0, n):

        for j in range(0, i):

            x[i] = x[i] - L[i, j] * x[j]

        x[i] = x[i] / L[i, i]

    return x

def main():

    A_in = """
            1 0 0 0

            0 1 0 0

            1 3 1 0

            4 1 2 1
                """

    b_in= """
            1

            1

            2

            0
            """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    b = b.reshape(b.shape[0], 1)

    x = fsolve(A, b)

    print(x)

#main()
