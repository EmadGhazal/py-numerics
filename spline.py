import numpy as np

from nestm import nestm

import matplotlib.pyplot as plt

from gaussp import gaussp as gauss

def spline(x, y, t):

    n = x.size

    A = np.zeros((n, n))

    b = np.zeros(n)

    d = np.zeros(n - 1)

    D = np.zeros(n - 1)

    for i in range(n - 1):

        d[i] = x[i + 1] - x[i]

        D[i] = y[i + 1] - y[i]

    for i in range(1, n - 1):

        A[i, i - 1:i + 2] = [d[i - 1], 2.0 * (d[i - 1] + d[i]), d[i]]

        b[i] = 3.0 * (D[i] / d[i] - D[i - 1] / d[i - 1])

    if t == "n":

        A[0, 0] = 1.0

        A[n - 1, n - 1] = 1.0

    if t == "v":

        A[0, 0] = 2.0

        A[n - 1, n - 1] = 2.0

        b[0] = 3.0

        b[n - 1] = 2.0

    if t == "c":

        A[0, 0:2] = [2.0 * d[0], d[0]]

        A[n - 1, n - 2:n] = [d[n - 2], 2 * d[n - 2]]

        b[0] = 3.0 * (D[0] / d[0] - 66789035.7)

        b[n - 1] = 3.0 * (79794975.1 - D[n - 2] / d[n - 2])

    if t == "p":

        A[0, 0:2] = [1.0, -1.0]

        A[n - 1, n - 2:n] = [1.0, -1.0]

    if t == "k":

        A[0, 0:3] = [d[1], -(d[0] + d[1]), d[0]]

        A[n - 1, n - 3:n] = [d[n - 2], -(d[n - 3] + d[n - 2]), d[n - 3]]

    c = np.zeros((n, 3))

    c[:, 1] = gauss(A, b)

    for i in range(n - 1):

        c[i, 2] = (c[i + 1, 1] - c[i, 1]) / (3.0 * d[i])

        c[i, 0] = D[i] / d[i] - d[i] / 3.0 * (2.0 * c[i, 1] + c[i + 1, 1])

    c = c[0:n - 1, 0:3]

    return c

def plotp(x, y, c):

    n = x.size

    xpp = np.array([])

    ypp = np.array([])

    for i in range(n - 1):

        xp = np.linspace(x[i], x[i + 1], int((x[i + 1] - x[i]) * 100.0))

        dx = xp - x[i]

        yp = c[i, 2] * dx

        yp = (yp + c[i, 1]) * dx

        yp = (yp + c[i, 0]) * dx + y[i]

        xpp = np.append(xpp, xp)

        ypp = np.append(ypp, yp)

    plt.plot(xpp, ypp)

    plt.plot(x, y, "o")

    plt.grid()

    plt.show()

    return None
