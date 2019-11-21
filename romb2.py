import numpy as np

from math import *

def romb2(f, a, b, tol):

    h = b - a

    R = np.array([[h / 2 * (f(a) + f(b))]])

    while True:

        n = R.shape[0]

        Rp = np.zeros((n + 1, n + 1))

        Rp[0:n, 0:n] = R

        R = np.copy(Rp)

        n = R.shape[0]

        h = h / 2

        sig = 0

        for j in range(1, 2 ** (n - 2) + 1):

            sig = sig + f(a + (2 * j - 1) * h)

        R[n - 1, 0] = 1 / 2 * R[n - 2, 0] + h * sig

        for j in range(1, n):

            R[n - 1, j] = (4 ** j * R[n - 1, j - 1] - R[n - 2, j - 1]) / (4 ** j - 1)

        if abs(R[n - 1, n - 1] - R[n - 2, n - 2]) < tol:

            break

    return R

def main():

    R = romb2(lambda x: log(x), 1, 2, 0.5 * 10 ** -15)

    print(R)

main()
