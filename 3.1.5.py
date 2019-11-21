import numpy as np

from nestm import nestm

from math import pi, sqrt, tan

def newtondd(x, y):

    n = x.size

    A = np.zeros((n, n))

    A[0:n, 0] = y[0:n]

    for i in range(1, n):

        for j in range(n - i):

            A[j, i] = (A[j + 1, i - 1] - A[j, i - 1]) / (x[j + i] - x[j])

    return A[0]

def main(x):

    b = np.array([0.0, pi / 12.0, pi / 6.0, pi / 4.0])

    c = newtondd(b, np.array([0.0, (sqrt(3.0) - 1.0) / (sqrt(3.0) + 1.0), 1.0 / sqrt(3.0), 1.0]))

    x = x % pi

    if x == pi / 2.0:

        print("Error.")

        return None

    if x >= 0.0 and x <= pi / 4.0:

        y = nestm(c, b, x)

    if x > pi / 4.0 and x < pi / 2.0:

        x = pi / 2.0 - x

        y = 1.0 / nestm(c, b, x)

    if x > pi / 2.0 and x <= 3.0 * pi / 4.0:

        x = x - pi / 2.0

        y = -1.0 / nestm(c, b, x)

    if x > 3.0 * pi / 4.0 and x < pi:

        x = pi - x

        y = -nestm(c, b, x)

    return y

x = np.linspace(0.0, pi / 4.0, 100000)

y = np.array([])

for element in x:

   y = np.append(y, abs(main(element) - tan(element)))

print(x[np.argmax(y)])
