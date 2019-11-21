import numpy as np

from nestm import nestm

from math import pi, sqrt, sin, cos

import matplotlib.pyplot as plt

from newtondd import newtondd as newton

def main(x):

    x1 = pi / 4.0 * cos(pi / 8.0) + pi / 4.0

    x2 = pi / 4.0 * cos(3.0 * pi / 8.0) + pi / 4.0

    x3 = pi / 4.0 * cos(5.0 * pi / 8.0) + pi / 4.0

    x4 = pi / 4.0 * cos(7.0 * pi / 8.0) + pi / 4.0

    b = np.array([x1, x2, x3, x4])

    c = newton(b, np.array([sin(x1), sin(x2), sin(x3), sin(x4)]))

    x = x % (2.0 * pi)

    if x >= 0.0 and x <= pi / 2.0:

        y = nestm(c, b, x)

    if x > pi / 2.0 and x <= pi:

        x = pi - x

        y = nestm(c, b, x)

    if x > pi and x <= 3.0 * pi / 2.0:

        x = x - pi

        y = -nestm(c, b, x)

    if x > 3.0 * pi / 2.0 and x < 2.0 * pi:

        x = 2 * pi - x

        y = -nestm(c, b, x)

    return y

x = np.linspace(-2, 2, 400)

y1 = np.array([])

for element in x:

    y1 = np.append(y1, main(element))

y2 = np.sin(x)

plt.plot(x, y1, "r")

plt.plot(x, y2, "b")

plt.grid()

plt.show()
