import numpy as np

import numpy.linalg as LA

from io import StringIO

def houser(A):

    m = A.shape[0]

    n = A.shape[1]

    R = np.copy(A)

    for i in range(n):

        a = R[i:,i].reshape(m - i, 1)

        w = np.zeros((m - i, 1))

        w[0] = LA.norm(a)

        v = w - a

        if LA.norm(v) == 0:

            continue

        P =  np.matmul(v, np.transpose(v)) / np.dot(np.transpose(v), v)

        H = np.identity(m - i) - 2 * P

        if i == 0:

            Q = np.copy(H)

        else:

            Q[i:,:] = np.matmul(H, Q[i:,:])

        R[i:,i:] = np.matmul(H, R[i:,i:])

    Q = np.transpose(Q)

    while Q.shape[1] > n:

        Q = np.delete(Q, -1, axis = 1)

        R = np.delete(R, -1, axis = 0)
    
    return Q, R

def main():

    A_in = """
            1 4

            -1 1

            1 1

            1 0
                """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    Q, R = houser(A)

    print(A, "\n")

    print(Q, "\n")

    print(R)

main()
