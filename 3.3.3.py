import numpy as np

from nestm import nestm

from math import pi, e, cos, log

import matplotlib.pyplot as plt

from newtondd import newtondd as newton

def main(x, c, b):

    k = 0

    if x < 1.0:

        k = -1

        while True:

            if x >= e ** k and x < e ** (k + 1):

                break

            k -= 1

    if x > e:

        k = 1

        while True:

            if x >= e ** k and x < e ** (k + 1):

                break

            k += 1

    x = x * e ** -k

    y = nestm(c, b, x) + k

    return y

n = 26

b = np.array([])

for i in range(1, n + 1):

    b = np.append(b, ((e - 1.0) / 2.0) * cos((2 * i - 1) * pi / 52.0) + ((e + 1.0) / 2.0))

yn = np.log(b)

c = newton(b, yn)

x = np.linspace(10 ** -4, 10 ** 4, 10 ** 5)

y1 = np.array([])

for element in x:

    y1 = np.append(y1, main(element, c, b))

y2 = np.log(x)

plt.plot(x, y1, "r")

plt.plot(x, y2, "b")

plt.grid()

plt.show()
