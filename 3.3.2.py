import numpy as np

from nestm import nestm

from math import pi, sqrt, sin, cos

import matplotlib.pyplot as plt

from newtondd import newtondd as newton

def main(x, c, b):

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

n = 10

b = np.array([])

for i in range(1, n + 1):

    b = np.append(b, pi / 4.0 * cos((2 * i - 1) * pi / 20.0) + pi / 4.0)

yn = np.cos(b)

c = newton(b, yn)

x = np.linspace(-10, 10, 2 * 10 ** 4)

y1 = np.array([])

for element in x:

    y1 = np.append(y1, main(element, c, b))

y2 = np.cos(x)

plt.plot(x, y1, "r")

plt.plot(x, y2, "b")

plt.grid()

plt.show()
