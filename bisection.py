from math import *

import sys

def bisection(f, a, b, tol):

    iterate = []

    error = []

    rel_error = [0.0]

    fa = f(a)

    fb = f(b)

    if not (fa * fb < 0):

        print "Error: the interval provided does not contain a root."

        sys.exit()

    while True:

        iterate.append((a + b) / 2.0)

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

    for i in xrange(len(iterate)):

        error.append(abs(iterate[i] - iterate[-1]))

    for i in xrange(1, len(error)):

        rel_error.append(error[i] / error[i - 1])

    return iterate, error, rel_error

iterate, error, rel_error = bisection(lambda x: 1.0 / x, -2.0, 1.0, 0.5 * (10 ** (-8)))

for i in xrange(len(iterate)):

    print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])
