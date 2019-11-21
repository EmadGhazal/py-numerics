import numpy as np

from nestm import nestm

from math import pi, sqrt, cos

import matplotlib.pyplot as plt

def newtondd(x, y):

    n = x.size

    A = np.zeros((n, n))

    A[0:n, 0] = y[0:n]

    for i in range(1, n):

        for j in range(n - i):

            A[j, i] = (A[j + 1, i - 1] - A[j, i - 1]) / (x[j + i] - x[j])

    return A[0]

def main(x):

    b = np.array([0.0, pi / 6.0, pi / 3.0, pi / 2.0])

    c = newtondd(b, np.array([1.0, sqrt(3.0) / 2.0, 0.5, 0.0]))

    x = x % (2.0 * pi)

    if x >= 0.0 and x <= pi / 2.0:

        y = nestm(c, b, x)

    if x > pi / 2.0 and x <= pi:

        x = pi - x

        y = -nestm(c, b, x)

    if x > pi and x <= 3.0 * pi / 2.0:

        x = x - pi

        y = -nestm(c, b, x)

    if x > 3.0 * pi / 2.0 and x < 2.0 * pi:

        x = 2 * pi - x

        y = nestm(c, b, x)

    return y

x = np.linspace(-2 * pi, 2 * pi, 1250)

y = np.array([])

for element in x:

    y = np.append(y, abs(main(element) - cos(element)))

plt.plot(x, y)

plt.grid()

plt.show()
