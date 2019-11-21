import numpy as np

from math import *

def romb1(f, a, b, n):

    h = b - a

    R = np.zeros((n, n))

    R[0, 0] = h / 2 * (f(a) + f(b))

    for i in range(1, n):

        h = h / 2

        sig = 0

        for j in range(1, 2 ** (i - 1) + 1):

            sig = sig + f(a + (2 * j - 1) * h)

        R[i, 0] = 1 / 2 * R[i - 1, 0] + h * sig

        for j in range(1, i + 1):

            R[i, j] = (4 ** j * R[i, j - 1] - R[i - 1, j - 1]) / (4 ** j - 1)

    return R

def main():

    R = romb1(lambda x: x / sqrt(x ** 4 + 1), 0, 1, 5)

    print(R)

    print(abs(R[4, 4] - 1/2 * log(sqrt(2) + 1)))

main()
