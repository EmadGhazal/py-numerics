import numpy as np

import numpy.linalg as LA

from gaussp import gaussp as gauss

from io import StringIO

from math import sqrt

def normal(A, b):

    Ap = np.matmul(np.transpose(A), A)

    bp = np.matmul(np.transpose(A), b)

    return gauss(Ap, bp)

def err2(A, b, x):

    return LA.norm(b - np.matmul(A, x))

def errs(A, b, x):

    return LA.norm(b - np.matmul(A, x)) ** 2

def rmse(A, b, x):

    res = b - np.matmul(A, x)

    size = res.shape[0]

    return sqrt(LA.norm(res) ** 2 / size)

def main():

    A_in = """
            4 2 3 0

            -2 3 -1 1

            1 3 -4 2

            1 0 1 -1

            3 1 3 -2
                """

    b_in = """
            10

            0

            2

            0

            5
            """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    b = b.reshape(b.size, 1)

    x = normal(A, b)

    e2rr = err2(A, b, x)

    serr = errs(A, b, x)

    erms = rmse(A, b, x)

    print(x)

    print(e2rr, serr, erms)

#main()
