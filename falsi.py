from math import *

import sys

def falsi(f, a, b, tol):

    iterate = []

    error = []

    rel_error = [0.0]

    fa = f(a)

    fb = f(b)

    if not (fa * fb < 0):

        print "Error: the interval provided does not contain a root."

        sys.exit()

    while True:

        iterate.append((b * fa - a * fb) / (fa - fb))

        fc = f(iterate[-1])

        if len(iterate) >= 2 and abs(iterate[-1] - iterate[-2]) < tol:

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

iterate, error, rel_error = falsi(lambda x: x ** 3 - 2.0 * x ** 2 + 1.5 * x, 1.0, 2.0, 0.5 * (10 ** (-8)))

for i in xrange(len(iterate)):

    print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])
