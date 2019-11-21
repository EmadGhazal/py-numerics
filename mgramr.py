import numpy as np

import numpy.linalg as LA

from io import StringIO

def mgramr(A):

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
        
    return Q, R

def main():

    A_in = """
            1 1

            0 0

            0 1
                """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    Q, R = mgramr(A)

    print(A, "\n")

    print(Q, "\n")

    print(R)

main()
