import numpy as np

from math import *

import matplotlib.pyplot as plt

def fourrk(f, y0, n, b):

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        s1 = f(t[-1], w[-1])

        s2 = f(t[-1] + h / 2, w[-1] + h / 2 * s1)

        s3 = f(t[-1] + h / 2, w[-1] + h / 2 * s2)

        s4 = f(t[-1] + h, w[-1] + h * s3)

        w = np.append(w, w[-1] + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4))

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

        h = np.array([])

        err = np.array([])

        for j in range(6):

            n = 10 * 2 ** j

            h = np.append(h, 1 / n)

            t, w = fourrk(g[i], 1, n, 1)

            err = np.append(err, abs(w[-1] - f[i](1)))

        print(log(err[-1] / err[-2]) / log(h[-1] / h[-2]))

        plt.plot(h, err)

        plt.grid()

        plt.loglog()

        plt.show()

#main()
