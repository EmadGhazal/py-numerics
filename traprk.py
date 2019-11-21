import numpy as np

from math import *

import matplotlib.pyplot as plt

from euler import euler

def trape(f, y0, n, b):

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        fp = f(t[-1], w[-1])

        w = np.append(w, w[-1] + h/2 * (fp + f(t[-1] + h, w[-1] + h * fp)))

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

    ya = 2

    fi = lambda t: 2 * atanh(exp(t) * tanh(ya / 2))

    gi = lambda t, y: sinh(y)

    h = np.array([])

    err = np.array([])

    for i in range(6):

        n = 10 * 2 ** i

        h = np.append(h, 1/ n)

        t, w = trape(gi, 2, n, 0.25)

        err = np.append(err, abs(fi(0.25) - w[-1]))

        plt.plot(t, w, label = str(i))

    fi = np.vectorize(fi)

    plt.plot(t, fi(t), label = "f")

    plt.grid()

    plt.legend()

    plt.show()

    plt.plot(h, err)

    plt.loglog()

    plt.grid()

    plt.show()

main()
