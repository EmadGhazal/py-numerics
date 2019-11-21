import numpy as np

from math import *

import matplotlib.pyplot as plt

def open3(f, a, b):

    h = (b - a) / 4

    return 4 * h / 3 * (2 * f(a + h) - f(a + 2 * h) + 2 * f(a + 3 * h))

def aopen3(f, a, b, tol):

    itr = 0

    sig = 0

    n = 1

    x = np.array([[a, b]], np.float)

    F = np.array([[f(a), f(b)]], np.float)

    TOL = np.array([tol])

    app = np.array([open3(f, a, b)])
    
    while n > 0:

        itr = itr + 1

        c = (x[n - 1, 0] + x[n - 1, 1]) / 2

        fc = f(c)

        appp = app[n - 1]

        app[n - 1] = open3(f, x[n - 1, 0], c)

        app = np.insert(app, n, open3(f, c, x[n - 1, 1]))

        if abs(appp - (app[n - 1] + app[n])) < 8 * TOL[n - 1]:

            sig = sig + (app[n - 1] + app[n])

            n = n - 1

        else:

            x = np.insert(x, n, [c, x[n - 1, 1]], axis = 0)

            F = np.insert(F, n, [fc, F[n - 1, 1]], axis = 0)

            x[n - 1] = [x[n - 1, 0], c]

            F[n - 1] = [F[n - 1, 0], fc]

            TOL[n - 1] = TOL[n - 1] / 2

            TOL = np.insert(TOL, n, TOL[n - 1])

            n = n + 1

    xpp = x[:, 0]

    xpp = np.append(xpp, x[-1, 1])

    Fpp = F[:, 0]

    Fpp = np.append(Fpp, F[-1, 1])

    xp = np.linspace(a, b, int(100 * abs(b - a)))

    fp = np.vectorize(f)

    yp = fp(xp)

    plt.plot(xp, yp, "r")

    plt.plot(xpp, Fpp, "k")

    plt.xticks(xpp)

    plt.grid()

    plt.show()

    return sig, itr

def main():

    print(aopen3(lambda x: x / sqrt(x ** 4 + 1), 0, 1, 0.5 * 10 ** -8))

main()
