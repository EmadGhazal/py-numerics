import numpy as np

from math import *

import matplotlib.pyplot as plt

def meuler(f, y0, n, b):

    m = y0.shape[0]

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        w = np.append(w, [w[-1] + h * f(t[-1], w[-1])], axis = 0)

        t = np.append(t, t[-1] + h)

    return t, w

def main():

    y0 = np.array([1, 0])

    f = lambda t, y: np.array([-y[1], y[0]])

    y = lambda t: np.array([cos(t), sin(t)])

    t, w = meuler(f, y0, 4, 1)

    print(t)

    print(w)

    print(abs(y(1) - w[-1]))

#main()
