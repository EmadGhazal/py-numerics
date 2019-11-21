import numpy as np

from math import *

import matplotlib.pyplot as plt

def midrk(f, y0, n, b):

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        w = np.append(w, w[-1] + h * f(t[-1] + h / 2, w[-1] + h / 2 * f(t[-1], w[-1])))

        t = np.append(t, t[-1] + h)

    return t, w

def main():

    f = [lambda t: 1 + t ** 2 / 2,

         lambda t: exp(t ** 3 / 3),

         lambda t: exp(t ** 2 + 2 * t),

         lambda t: exp(t ** 5),

         lambda t: (3 * t + 1) ** (1/3),

         lambda t: (3 * t ** 4 / 4 + 1) ** (1/3),

         lambda t: exp(t) - t - 1,

         lambda t: exp(-t) + t - 1,

         lambda t: exp(-2 * t) + 2 * t - 1]

    g = [lambda t, y: t,

         lambda t, y: t ** 2 * y,

         lambda t, y: 2 * (t + 1) * y,

         lambda t, y: 5 * t ** 4 * y,

         lambda t, y: 1 / y ** 2,

         lambda t, y: t ** 3 / y ** 2,

         lambda t, y: t + y,

         lambda t, y: t - y,

         lambda t, y: 4 * t - 2 * y]

    for i in range(len(f)):

        t, w = midrk(g[i], 1, 10, 1)

        print(t, "\n")

        print(w, "\n")

        for j in range(t.shape[0]):

            print(abs(f[i](t[j]) - w[j]), "\n")

#main()
