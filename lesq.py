import numpy as np

from normal import normal

from nestm import nestm as nest

from io import StringIO

import matplotlib.pyplot as plt

from math import pi, e, sin, cos, exp, sqrt

def error(x, y, c, typ):

    if typ == "l" or typ == "q" or typ == "c":

        yp = nest(np.flip(c), np.array([]), x)

        err2 = sum(abs(y - yp) ** 2)

        err = sqrt(err2)

        rmse = sqrt(err2 / x.shape[0])

    if typ == "p1":

        f = lambda x: c[0] + c[1] * cos(2.0 * pi * x) + c[2] * sin(2.0 * pi * x)

        f = np.vectorize(f)

        yp = f(x)

        err2 = sum(abs(y - yp) ** 2)

        err = sqrt(err2)

        rmse = sqrt(err2 / x.shape[0])

    if typ == "p2":

        f = lambda x: c[0] + c[1] * cos(2.0 * pi * x) + c[2] * sin(2.0 * pi * x) + c[3] * cos(4.0 * pi * x)

        f = np.vectorize(f)

        yp = f(x)

        err2 = sum(abs(y - yp) ** 2)

        err = sqrt(err2)

        rmse = sqrt(err2 / x.shape[0])

    if typ == "e":

        f = lambda x: c[0] * exp(c[1] * x)

        f = np.vectorize(f)

        yp = f(x)

        err2 = sum(abs(y - yp) ** 2)

        err = sqrt(err2)

        rmse = sqrt(err2 / x.shape[0])

    if typ == "d":

        f = lambda x: c[0] * x * exp(c[1] * x)

        f = np.vectorize(f)

        yp = f(x)

        err2 = sum(abs(y - yp) ** 2)

        err = sqrt(err2)

        rmse = sqrt(err2 / x.shape[0])

    return err2, err, rmse

def lesq(x, y, typ):

    if typ == "l":

        A = np.ones((x.shape[0], 2))

        A[:,0] = x

        c = normal(A, y)

        err2, err, rmse = error(x, y, c, typ)

    if typ == "q":

        A = np.ones((x.shape[0], 3))

        A[:,0] = x ** 2

        A[:,1] = x

        c = normal(A, y)

        err2, err, rmse = error(x, y, c, typ)

    if typ == "c":

        A = np.ones((x.shape[0], 4))

        A[:,0] = x ** 3

        A[:,1] = x ** 2

        A[:,2] = x

        c = normal(A, y)

        err2, err, rmse = error(x, y, c, typ)

    if typ == "p1":

        A = np.ones((x.shape[0], 3))

        A[:,1] = np.cos(2.0 * pi * x)

        A[:,2] = np.sin(2.0 * pi * x)

        c = normal(A, y)

        err2, err, rmse = error(x, y, c, typ)

    if typ == "p2":

        A = np.ones((x.shape[0], 4))

        A[:,1] = np.cos(2.0 * pi * x)

        A[:,2] = np.sin(2.0 * pi * x)

        A[:,3] = np.cos(4.0 * pi * x)

        c = normal(A, y)

        err2, err, rmse = error(x, y, c, typ)

    if typ == "e":

        A = np.ones((x.shape[0], 2))

        A[:,1] = x

        c = normal(A, np.log(y))

        err2, err, rmse = np.zeros(2), np.zeros(2), np.zeros(2)

        err2[0], err[0], rmse[0] = error(x, np.log(y), np.flip(c), "l")

        c[0] = exp(c[0])

        err2[1], err[1], rmse[1] = error(x, y, c, typ)

    if typ == "d":

        A = np.ones((x.shape[0], 2))

        A[:,1] = x

        c = normal(A, np.log(y / x))

        err2, err, rmse = np.zeros(2), np.zeros(2), np.zeros(2)

        err2[0], err[0], rmse[0] = error(x, np.log(y / x), np.flip(c), "l")

        c[0] = exp(c[0])

        err2[1], err[1], rmse[1] = error(x, y, c, typ)
        
    return c, err2, err, rmse

def plot(x, y, c, typ):

    xp = np.linspace(np.amin(x), np.amax(x), int((np.amax(x) - np.amin(x)) * 100))

    if typ == "l" or typ == "q" or typ == "c":

        yp = nest(np.flip(c), np.array([]), xp)

    if typ == "p1":

        f = lambda x: c[0] + c[1] * cos(2.0 * pi * x) + c[2] * sin(2.0 * pi * x)

        f = np.vectorize(f)

        yp = f(xp)

    if typ == "p2":

        f = lambda x: c[0] + c[1] * cos(2.0 * pi * x) + c[2] * sin(2.0 * pi * x) + c[3] * cos(4.0 * pi * x)

        f = np.vectorize(f)

        yp = f(xp)

    if typ == "e":

        f = lambda x: c[0] * exp(c[1] * x)

        f = np.vectorize(f)

        yp = f(xp)

    if typ == "d":

        f = lambda x: c[0] * x * exp(c[1] * x)

        f = np.vectorize(f)

        yp = f(xp)

    plt.plot(xp, yp, "r")

    plt.plot(x, y, "ob")

    plt.grid()

    plt.show()

    return None

def main(typ):

    points = """
                """

    points = np.genfromtxt(StringIO(points), delimiter = " ")

    x = points[:,0]

    y = points[:,1]

    c, err2, err, rmse = lesq(x, y, typ)

    print(c)

    print(err2, err, rmse)

    plot(x, y, c, typ)

main("l")
