import numpy as np

from math import *

#import numba

#@numba.jit(nopython = True)

def mfourrk(f, y0, n, b):

    m = y0.shape[0]

    l = int(n * b)

    w = np.zeros((l + 1, m))

    w[0, :] = y0

    t = np.zeros(l + 1)

    h = 1 / n

    for i in range(l):
        
        s1 = f(t[i], w[i])

        s2 = f(t[i] + h / 2, w[i] + h / 2 * s1)

        s3 = f(t[i] + h / 2, w[i] + h / 2 * s2)

        s4 = f(t[i] + h, w[i] + h * s3)

        w[i + 1, :] = w[i] + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)

        t[i + 1] = t[i] + h

    return t, w

#@numba.jit(nopython = True)

def f(t, y):

    return np.array([y[0] + y[1], -y[0] + y[1]])

def main():

    y0 = np.array([1, 0])    

    #y = lambda t: np.array([exp(t) * cos(t), -exp(t) * sin(t)])

    t, w = mfourrk(f, y0, 200, 200)

    #print(t, "\n", w, "\n")

main()
