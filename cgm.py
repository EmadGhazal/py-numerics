import numpy as np

import numpy.linalg as LA

import scipy.linalg as SLA

import matplotlib.pyplot as plt

def cgm(A, b, x0, n):

    x = np.copy(x0)

    r = b - np.dot(A, x)

    d = np.copy(r)

    itr = 0

    err = np.array([], dtype = np.float)

    while True:

        err = np.append(err, LA.norm(r, np.inf))

        if err[-1] < 0.5 * 10 ** -6:

            break

        a = np.dot(r, r) / np.dot(d, np.dot(A, d))

        x = x + a * d

        rtemp = np.copy(r)

        r = r - a * np.dot(A, d)

        b = np.dot(r, r) / np.dot(rtemp, rtemp)

        d = r + b * d

        itr += 1

    return x, err, itr

def cgmj(A, b, x0, n):

    x = np.copy(x0)

    r = b - np.dot(A, x)

    J = np.diag(np.reciprocal(np.diag(A)))

    z = np.dot(J, r)

    d = np.copy(z)

    itr = 0

    err = np.array([], dtype = np.float)

    while True:

        err = np.append(err, LA.norm(r, np.inf))

        if err[-1] < 0.5 * 10 ** -6:

            break

        a = np.dot(r, z) / np.dot(d, np.dot(A, d))

        x = x + a * d

        rtemp = np.copy(r)

        r = r - a * np.dot(A, d)

        ztemp = np.copy(z)

        z = np.dot(J, r)

        b = np.dot(r, z) / np.dot(rtemp, ztemp)

        d = z + b * d

        itr += 1

    return x, err, itr

def main():

    n = 195

    #A = np.array([[1, -1, 0], [-1, 2, 1], [0, 1, 5]], dtype = np.float)

    #b = np.array([3, -3, 4], dtype = np.float)

    C = np.zeros((n, n), dtype = np.float)

    D = np.zeros((n, n), dtype = np.float)

    for i in range(n):

        for j in range(n):

            if j == i:

                C[i][j] = 2.0

            if j == i + 3:

                C[i][j] = 0.1

                C[j][i] = 0.1

            if j == i + 39:

                C[i][j] = 0.5

                C[j][i] = 0.5

            if j == i + 42:

                C[i][j] = 0.5

                C[j][i] = 0.5

    X = SLA.block_diag(C, C, C, C)

    Y = np.roll(SLA.block_diag(0.5 * C, D, D, D), 1, axis = 1)

    Z = np.roll(SLA.block_diag(0.5 * C, D, D, D), -1, axis = 1)

    A = X + Y + Z

    b = np.dot(A, np.ones(n * 4, dtype = np.float))

    x, err, itr = cgm(A, b, np.zeros(n * 4, dtype = np.float), n * 4)

    xj, errj, itrj = cgmj(A, b, np.zeros(n * 4, dtype = np.float), n * 4)

    print(itr, itrj)

    plt.plot(np.arange(0, err.size), err, "ro")

    plt.plot(np.arange(0, errj.size), errj, "bo")

    plt.grid()

    plt.show()

main()
