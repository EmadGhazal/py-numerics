from math import log, pi, cos, sqrt, exp, sin

import numpy as np

import matplotlib.pyplot as plt

def trap(f, a, b, m):

    h = (b - a) / m

    sig = 0

    for i in range(1, m):

        sig = sig + f(a + i * h)

    return h / 2 * (f(a) + f(b) + 2 * sig), (b - a) * h ** 2 / 12

def main():

    f = lambda x: x / sqrt(x ** 2 + 9)

    x = np.array([])

    y = np.array([])

    h = 4

    for i in range(9):

        x = np.append(x, h / 2 ** i)

        y = np.append(y, abs(trap(f, 0, 4, 2 ** i)[0] - 2))

    print(log(y[-1]/y[-2]) / log(x[-1]/x[-2]))

    plt.plot(x, y)

    plt.xscale("log")

    plt.yscale("log")

    plt.grid()

    plt.show()

main()
