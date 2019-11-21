import numpy as np

from nestm import nestm

from math import pi, e, cos, exp

import matplotlib.pyplot as plt

from newtondd import newtondd as newton

n = 11

b1 = np.array([])

b2 = np.array([])

for i in range(n):

    b1 = np.append(b1, -1.0 + i * 2.0 / 10.0)

for i in range(1, n + 1):

    b2 = np.append(b2, cos((2 * i - 1) * pi / 22.0))

yn1 = np.exp(-b1 ** 2)

yn2 = np.exp(-b2 ** 2)

c1 = newton(b1, yn1)

c2 = newton(b2, yn2)

x = np.linspace(-1.0, 1.0, 201)

y1 = nestm(c1, b1, x)

y2 = nestm(c2, b2, x)

y3 = np.exp(-x ** 2)

plt.plot(x, abs(y1 - y3), "r")

plt.plot(x, abs(y2 - y3), "b")

#plt.plot(x, y3, "g")

plt.grid()

plt.show()
