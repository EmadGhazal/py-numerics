import numpy as np

import numpy.linalg as LA

from io import StringIO

from normal import normal, err2

def mgram(A):

    m = A.shape[0]

    n = A.shape[1]

    Q = np.zeros((m, n))

    R = np.zeros((n, n))

    for i in range(n):

        a = A[:,i].reshape(m, 1)

        for j in range(i):

            q = Q[:,j].reshape(m, 1)

            R[j, i] = np.dot(np.transpose(q), a)

            a = a - q * R[j, i]

        R[i,i] = LA.norm(a)

        Q[:,i] = (a / R[i, i]).reshape(m)

    B = np.identity(m)

    b = np.zeros(m).reshape(m, 1)

    while Q.shape[1] < m:

        Qp = np.insert(Q, Q.shape[1], B[:,0], axis = 1)

        x = normal(Qp, b)

        if err2(Qp, b, x) == 0:

            Q = np.copy(Qp)

        B = np.delete(B, 0, axis = 1)

    r = np.zeros(n)

    for i in range(n, m):

        a = Q[:,i].reshape(m, 1)

        v = np.copy(a)

        for j in range(i):

            q = Q[:,j].reshape(m, 1)

            rji = np.dot(np.transpose(q), a)

            v = v - q * rji

        rii = LA.norm(v)

        Q[:,i] = (v / rii).reshape(m)

        R = np.insert(R, R.shape[0], r, axis = 0)
        
    return Q, R

def main():

    A_in = """
            1 1

            0 0

            0 1
                """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    Q, R = mgram(A)

    print(A, "\n")

    print(Q, "\n")

    print(R)

main()
