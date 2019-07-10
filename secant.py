from math import *

from stewart import f

def secant(f, x0, x1, tol):

    iterate = [x0, x1]

    error = []

    rel_error = [0]

    iterate.append(x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0)))

    while True:

        if abs(iterate[-1] - iterate[-2]) < tol:

            break

        iterate.append(iterate[-1] - (f(iterate[-1]) * (iterate[-1] - iterate[-2])) / (f(iterate[-1]) - f(iterate[-2])))

    for i in xrange(len(iterate)):

        error.append(abs(iterate[i] - iterate[-1]))

    for i in xrange(1, len(error)):

            rel_error.append(error[i] / (error[i - 1] ** ((1.0 + sqrt(5)) / 2.0)))

    return iterate, error, rel_error

iterate, error, rel_error = secant(f, 1.7, 1.8, 0.5 * (10 ** (-8)))

for i in xrange(len(iterate)):

    print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])
