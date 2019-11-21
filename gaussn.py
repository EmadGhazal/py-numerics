import numpy as np

import numpy.linalg as LA

from gaussp import gaussp as gauss

from math import exp, log, sqrt, cos, sin

from io import StringIO

import matplotlib.pyplot as plt

f = lambda x, t: x[0, 0] * exp(-x[1, 0] * t) * cos(x[2, 0] * t + x[3, 0])

J1 = lambda x, t: exp(-x[1, 0] * t) * cos(x[2, 0] * t + x[3, 0])

J2 = lambda x, t: x[0, 0] * cos(x[2, 0] * t + x[3, 0]) * exp(-x[1, 0] * t) * -t

J3 = lambda x, t: x[0, 0] * exp(-x[1, 0] * t) * -sin(x[2, 0] * t + x[3, 0]) * t

J4 = lambda x, t: x[0, 0] * exp(-x[1, 0] * t) * -sin(x[2, 0] * t + x[3, 0])

def gaussn(x0, x, y):

    n = x.shape[0]

    xp = np.copy(x0)

    while True:

        print(xp)

        xpp = np.copy(xp)

        J = np.zeros((n, 4))

        r = np.zeros((n, 1))

        for i in range(n):

            r[i, 0] = f(xpp, x[i, 0]) - y[i, 0]

            J[i, 0] = J1(xpp, x[i, 0])

            J[i, 1] = J2(xpp, x[i, 0])

            J[i, 2] = J3(xpp, x[i, 0])

            J[i, 3] = J4(xpp, x[i, 0])

        s = gauss(np.dot(np.transpose(J), J) + 20 * np.diag(np.diag(np.dot(np.transpose(J), J))), np.dot(-np.transpose(J), r))

        xp = xpp + s

        if LA.norm(s, np.inf) < 0.5 * 10 ** -6:

            break

    err = np.array([])

    for i in range(n):

        err = np.append(err, abs(f(xp, x[i, 0]) - y[i, 0]))

    rmse = sqrt(sum(err ** 2) / n)

    xppp = np.linspace(x[0], x[-1], int(abs(x[-1] - x[0]) * 100))

    yppp = np.array([])

    for element in xppp:

        yppp = np.append(yppp, f(xp, element))

    plt.plot(xppp, yppp, "b")

    plt.plot(x, y, "or")

    plt.grid()

    plt.show()

    return xp, rmse

def main():

    A_in = """
            1 2

            3 6

            4 4

            5 2

            6 -1

            8 -3
                    """

    A = np.genfromtxt(StringIO(A_in), delimiter = " ")

    x = A[:, 0]

    y = A[:, 1]

    x = x.reshape(x.shape[0], 1)

    y = y.reshape(y.shape[0], 1)

    x0 = np.array([[8.5], [0.3], [1], [1]])

    xp, rmse = gaussn(x0, x, y)

    print(xp)

    print(rmse)

main()
