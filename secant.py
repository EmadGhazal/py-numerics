from math import *

import numpy as np

def secant(f, x0, x1, tol):

    itr = np.array([x0, x1])

    err = np.array([])

    rerr = np.array([0.0])

    itr = np.append(itr, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0)))

    while True:

        if abs(itr[-1] - itr[-2]) < tol:

            break

        itr = np.append(itr, itr[-1] - (f(itr[-1]) * (itr[-1] - itr[-2])) / (f(itr[-1]) - f(itr[-2])))

    while True:

        if itr[-1] == itr[-2]:

            itr = np.delete(itr, -1)

            continue

        break

    for i in range(len(itr)):

        err = np.append(err, abs(itr[i] - itr[-1]))

    for i in range(1, len(err)):

            rerr = np.append(rerr, err[i] / (err[i - 1] ** ((1.0 + sqrt(5)) / 2.0)))

    return itr, err, rerr

def main():

    f = lambda x: 6 * cos(x) - x * sin(x)

    itr, err, rerr = secant(f, 1, 2, 0.5 * (10 ** (-6)))

    for i in range(len(itr)):

        print("{:19.16f}    {:19.16f}   {:19.16f}".format(itr[i], err[i], rerr[i]))

main()
