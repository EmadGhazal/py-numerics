import numpy as np

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from mfourrk import mfourrk as solve

a = 7

t0 = 50

d = 5

def sim(t, w, I):

    v = w[:, 0]

    m = w[:, 1]

    n = w[:, 2]

    h = w[:, 3]

    fig, ax = plt.subplots(3, 1)

    I = np.vectorize(I)

    ax[0].plot(t, I(t, t0, d))

    ax[1].plot(t, v)

    ax[2].plot(t, m, label = "m")

    ax[2].plot(t, n, label = "n")

    ax[2].plot(t, h, label = "h")

    ax[0].grid()

    ax[1].grid()

    ax[2].grid()

    plt.legend()

    plt.show()

    return None

def main():

    C = 1

    g1, g2, g3 = 120, 36, 0.3

    E0, E1, E2, E3 = -65, 50, -77, -54.4

    am = lambda v: (2.5 - 0.1 * v) / (exp(2.5 - 0.1 * v) - 1)

    bm = lambda v: 4 * exp(-v / 18)

    an = lambda v: (0.1 - 0.01 * v) / (exp(1 - 0.1 * v) - 1)

    bn = lambda v: 1/8 * exp(-v / 80)

    ah = lambda v: 0.07 * exp(-v / 20)

    bh = lambda v: 1 / (exp(3 - 0.1 * v) + 1)

    def I1(a, t, t0, d):

        if t >= t0 and t <= t0 + d:

            return a

        else:

            return 0

    def I2(t, t0, d):

        if t >= t0 and t <= t0 + d:

            return 14/5 * t - 140

        else:

            return 0

    y0 = np.array([-65, 0, 0.3, 0.6])

    f1 = lambda t, y: 1/C * (-g1 * y[1] ** 3 * y[3] * (y[0] - E1) - g2 * y[2] ** 4 * (y[0] - E2) - g3 * (y[0] - E3) + I2(t, t0, d))

    f2 = lambda t, y: (1 - y[1]) * am(y[0] - E0) - y[1] * bm(y[0] - E0)

    f3 = lambda t, y: (1 - y[2]) * an(y[0] - E0) - y[2] * bn(y[0] - E0)

    f4 = lambda t, y: (1 - y[3]) * ah(y[0] - E0) - y[3] * bh(y[0] - E0)

    f = lambda t, y: np.array([f1(t, y), f2(t, y), f3(t, y), f4(t, y)])

    t, w = solve(f, y0, 100, 100)

    sim(t, w, I2)

main()
