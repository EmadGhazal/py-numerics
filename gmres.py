import numpy as np

import numpy.linalg as LA

from io import StringIO

from lsqr import lsqr as ls

from fsolve import fsolve

from bsolve import bsolve

def gmres(A, b, x0, typ = None):

    flag = 1

    n = A.shape[0]

    if typ == "j":

        P = np.diag(A)

        P = 1/P

        P = np.diag(P)

    if typ == "g":

        D = np.diag(A)

        L = np.tril(A) - np.diag(D)

        PL = np.identity(n) + np.matmul(L, np.diag(1 / D))

        PU = np.triu(A)

    if typ == None:

        r = b - np.dot(A, x0)

    if typ == "j":

        r = np.dot(P, b - np.dot(A, x0))

    if typ == "g":

        r = bsolve(PU, fsolve(PL, b - np.dot(A, x0)))

    Q = r / LA.norm(r)

    H = np.zeros((n + 1, n))

    xpp = np.copy(x0)

    for i in range(n):

        xp = np.copy(xpp)

        if typ == None:

            v = np.dot(A, Q[:,i].reshape(n, 1))

        if typ == "j":

            v = np.dot(P, np.dot(A, Q[:,i].reshape(n, 1)))

        if typ == "g":

            v = bsolve(PU, fsolve(PL, np.dot(A, Q[:,i].reshape(n, 1))))

        for j in range(i + 1):

            H[j,i] = np.dot(np.transpose(Q[:,j]), v)

            v = v - H[j,i] * Q[:,j].reshape(n, 1)

        H[i + 1, i] = LA.norm(v)

        if H[i + 1, i] == 0:

            flag = 0

        else:

            Q = np.insert(Q, Q.shape[1], (v / H[i + 1,i])[:, 0], axis = 1)

        bp = np.zeros(i + 2).reshape(i + 2, 1)

        bp[0, 0] = LA.norm(r)

        c, e = ls(H[0:i + 2, 0:i + 1], bp)

        xpp = np.dot(Q[:, 0:i + 1], c)

        if LA.norm(xp - xpp, np.inf) < 0.5 * 10 ** -6:

            return x0 + xpp, i

        if flag == 0:

            break

    return x0 + xpp, i

def main():

    A_in = """
            1 0 9

            0 1 8

            0 0 1
                """

    b_in = """
            5

            4

            3
                """

    x_in = """
            2

            1

            0
                """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    b = np.genfromtxt(StringIO(b_in), delimiter = " ")

    x0 = np.genfromtxt(StringIO(x_in), delimiter = " ")

    b = b.reshape(b.shape[0], 1)

    x0 = x0.reshape(x0.shape[0], 1)

    x, itr = gmres(A, b, x0)

    print(x)

    print(itr)

main()
