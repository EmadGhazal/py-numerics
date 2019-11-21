import numpy as np

from nestm import nestm

import matplotlib.pyplot as plt

from math import exp

def newtondd(x, y):

    n = x.size

    A = np.zeros((n, n))

    A[0:n, 0] = y[0:n]

    for i in range(1, n):

        for j in range(n - i):

            A[j, i] = (A[j + 1, i - 1] - A[j, i - 1]) / (x[j + i] - x[j])

    return A[0]

def plotp(c, b):

    x = np.linspace(b[0], b[-1], int((b[-1] - b[0]) * 100))

    y = nestm(c, b, x)

    plt.plot(x, y)

    plt.grid()

    plt.show()

    return None
