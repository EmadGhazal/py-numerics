import numpy as np

from numpy import linalg as LA

import scipy.sparse as sp

from io import StringIO

def jacobi(A, b, x0):

    itr = 0

    n = A.shape[0]

    LU = A - np.diagflat(np.diag(A))

    xk1 = np.copy(x0)

    while True:

        print(xk1)

        xk = np.copy(xk1)

        for i in range(n):

            xk1[i] = (b[i] - np.matmul(LU[i], xk)) / A[i][i]

        itr += 1

        if LA.norm(xk1 - xk, np.inf) < 0.5 * 10 ** -6:

            break

    return xk1, itr

def jacobis(LU, Dinv, b, x0, n):

    itr = 0

    xk1 = np.copy(x0)

    while True:

        #print(xk1)

        xk = np.copy(xk1)

        xk1 = Dinv.dot(b - LU.dot(xk))

        itr += 1

        if LA.norm(xk1 - xk, np.inf) < 0.5 * 10 ** -3:

            break

    return xk1, itr

def main(typ = None):

    if typ == "s":

        n = 100

        D = sp.diags([2.0], [0], shape = (n, n), format = "csr", dtype = np.float)

        Dinv = sp.diags([1.0 / 2.0], [0], shape = (n, n), format = "csr", dtype = np.float)

        #X = sp.diags([0.5], [0], shape = (n, n), format = "lil", dtype = np.float)

        #X[n // 2 - 1 : n // 2 + 1, n // 2 - 1 : n // 2 + 1] = 0.0

        #X = np.flip(X, 1)

        #Y = sp.diags([-1.0, -1.0], [-1, 1], shape = (n, n), format = "lil", dtype = np.float)

        #LU = X + Y

        LU = sp.diags([1.0, 1.0], [-1, 1], shape = (n, n), format = "csr", dtype = np.float)

        #LU = LU.tocsr()

        b = np.full(n, 0.0)

        b[0], b[n - 1] = 1.0, -1.0

        #b[n // 2 - 1], b[n // 2] = 1.0, 1.0

        x0 = np.zeros(n)

        x, itr = jacobis(LU, Dinv, b, x0, n)

        print(itr)

        print(x)

        print(LA.norm(b - (LU + D).dot(x), np.inf))

    else:

        A = """
             3 -1 1

             1 -8 -2

             1 1 5
                            """

        b = """
                -2

                1

                4
                    """

        x0 = """
                0

                0

                0
                    """

        A = np.genfromtxt(StringIO(A), delimiter = " ")

        b = np.genfromtxt(StringIO(b), delimiter = " ")

        x0 = np.genfromtxt(StringIO(x0), delimiter = " ")

        x, itr = jacobi(A, b, x0)

        print(itr)

        print(x)

        print(LA.norm(b - np.matmul(A, x), np.inf))

main("s")
