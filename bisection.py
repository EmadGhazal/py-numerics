from math import *

import sys

import numpy as np

def bisection(f, a, b, tol):

    iterate = np.array([])

    error = np.array([])

    rel_error = np.array([0.0])

    fa = f(a)

    fb = f(b)

    if not (fa * fb < 0):

        print("Error: the interval provided does not contain a root.")

        return None

    while True:

        iterate = np.append(iterate, (a + b) / 2.0)

        fc = f(iterate[-1])

        if fc == 0 or (b - a) / 2.0 < tol:

            break

        else:

            if fa * fc < 0:

                b = iterate[-1]

                fb = fc

            else:

                a = iterate[-1]

                fa = fc

    for i in range(len(iterate)):

        error = np.append(error, abs(iterate[i] - iterate[-1]))

    for i in range(1, len(error)):

        rel_error = np.append(rel_error, error[i] / error[i - 1])

    #return iterate, error, rel_error

    return iterate[-1]

def main():

    #iterate, error, rel_error = bisection(lambda x: cos(x) - x, 0, 1.0, 0.5 * (10 ** (-6)))

    #for i in range(len(iterate)):

        #print("{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i]))

    iterate = bisection(lambda x: cos(x) - x, 0, 1.0, 0.5 * (10 ** (-6)))

    print(iterate)

#main()
