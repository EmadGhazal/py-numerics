from math import *

import numpy as np

def newton(f, fp, x0, tol, m = 1):

    itr = np.array([x0])

    err = np.array([])

    rerr = np.array([0])

    itr = np.append(itr, x0 - ((m * f(x0)) / fp(x0)))

    while True:

        if abs(itr[-1] - itr[-2]) < tol:

            break

        itr = np.append(itr, itr[-1] - ((m * f(itr[-1])) / fp(itr[-1])))

    for i in range(len(itr)):

        err = np.append(err, abs(itr[i] - itr[-1]))

    for i in range(1, len(err)):

        if m == 1:

            rerr = np.append(rerr, err[i] / (err[i - 1] ** 2))

        else:

            rerr = np.append(rerr, err[i] / err[i - 1])

    #return iterate, error, rel_error

    return itr[-1]

def main():

    #iterate, error, rel_error = newton(lambda x: x ** 4 - 12.0 * x ** 2 - 44.0, lambda x: 4.0 * x ** 3 - 24.0 * x, 0.9, 0.5 * (10 ** (-8)))

    #for i in xrange(len(iterate)):

        #print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])

    itr = newton(lambda x: x ** 4 - 12.0 * x ** 2 - 44.0, lambda x: 4.0 * x ** 3 - 24.0 * x, 0.9, 0.5 * (10 ** (-8)))

    print(itr)

#main()
