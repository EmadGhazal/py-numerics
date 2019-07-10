from math import *

import matplotlib.pyplot as plt

L1 = 3.0

L2 = 3.0 * sqrt(2)

L3 = 3.0

g = pi / 4.0

x1 = 5.0

x2 = 0.0

y2 = 6.0

p1 = 5.0

p2 = 7.0

p3 = 3.0

A2 = lambda t: L3 * cos(t) - x1

B2 = lambda t: L3 * sin(t)

A3 = lambda t: L2 * cos(t+g) - x2

B3 = lambda t: L2 * sin(t+g) - y2

N1 = lambda t: B3(t) * (p2 ** 2 - p1 ** 2 - A2(t) ** 2 - B2(t) ** 2) - B2(t) * (p3 ** 2 - p1 ** 2 - A3(t) ** 2 - B3(t) ** 2)

N2 = lambda t: -A3(t) * (p2 ** 2 - p1 ** 2 - A2(t) ** 2 - B2(t) ** 2) + A2(t) * (p3 ** 2 - p1 ** 2 - A3(t) ** 2 - B3(t) ** 2)

D = lambda t: 2 * (A2(t) * B3(t) - B2(t) * A3(t))

f = lambda t: N1(t) ** 2 + N2(t) ** 2 - p1 ** 2 * D(t) ** 2

"""t = 1.77751357

u1 = N1(t) / D(t)

v1 = N2(t) / D(t)

u2 = u1 + L2 * cos(t + g)

v2 = v1 + L2 * sin(t + g)

u3 = u1 + L3 * cos(t)

v3 = v1 + L3 * sin(t)

plt.plot([u1, u2, u3, u1], [v1, v2, v3, v1], "y")

plt.plot([u1], [v1], "ro")

plt.plot([u2], [v2], "go")

plt.plot([u3], [v3], "bo")

plt.plot([0.0, x1, x2], [0.0, 0.0, y2], "co")

plt.plot([0.0, u1], [0.0, v1], "r")

plt.plot([x1, u3], [0.0, v3], "r")

plt.plot([x2, u2], [y2, v2], "r")

plt.grid()

plt.show()"""
