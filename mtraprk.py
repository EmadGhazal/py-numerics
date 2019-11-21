import numpy as np

from math import *

import numba

@numba.jit(nopython = True)

def mtraprk(f, y0, n, b):

    m = y0.shape[0]

    l = int(n * b)

    w = np.zeros((l + 1, m))

    w[0, :] = y0

    t = np.zeros(l + 1)

    h = 1 / n

    for i in range(l):

        fp = f(t[i], w[i])

        fpp = f(t[i] + h, w[i] + h * fp)

        w[i + 1, :] = w[i] + h/2 * (fp + fpp)

        t[i + 1] = t[i] + h

    return t, w

@numba.jit(nopython = True)

def f(t, y):

    return np.array([y[0] + y[1], -y[0] + y[1]])

def main():

    y0 = np.array([1, 0])

    #y = lambda t: np.array([3 * exp(-t) + 2 * exp(4 * t), -2 * exp(-t) + 2 * exp(4 * t)])

    t, w = mtraprk(f, y0, 500, 500)

    #print(t, "\n", w)

main()
