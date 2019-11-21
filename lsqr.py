import numpy as np

import numpy.linalg as LA

from io import StringIO

from house import house

import scipy.linalg as SLA

def lsqr(A, b):

    m = A.shape[0]

    n = A.shape[1]

    Q, R = house(A)

    Ap = R[0:n,0:n]

    bpp = np.dot(np.transpose(Q), b)

    bp = bpp[0:n]

    x = np.copy(bp)

    for i in range(n - 1, -1, -1):

        for j in range(i + 1, n):

            x[i] = x[i] - Ap[i][j] * x[j]

        x[i] = x[i] / Ap[i][i]

    e = LA.norm(bpp[n:m])

    return x, e

def main():

    A_in = """
            1

            0
                """

    b_in = """
            1

            0
                """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    if len(A.shape) == 1:

        A = A.reshape(A.shape[0], 1)

    b = b.reshape(b.shape[0], 1)

    x, e = lsqr(A, b)

    print(x)

    print(e)

#main()
