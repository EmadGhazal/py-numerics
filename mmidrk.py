import numpy as np

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

def mmidrk(f, y0, n, b):

    m = y0.shape[0]

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        fp = f(t[-1], w[-1])

        fpp = f(t[-1] + h / 2, w[-1] + h / 2 * fp)

        w = np.append(w, [w[-1] + h * fpp], axis = 0)

        t = np.append(t, t[-1] + h)

    return t, w

def main():

    y0 = np.array([5, 0])

    f = lambda t, y: np.array([y[0] + 3 * y[1], 2 * y[0] + 2 * y[1]])

    y = lambda t: np.array([3 * exp(-t) + 2 * exp(4 * t), -2 * exp(-t) + 2 * exp(4 * t)])

    t, w = mmidrk(f, y0, 4, 1)

    print(t, "\n", w, "\n")

    print(abs(w[-1] - y(1)))

main()
