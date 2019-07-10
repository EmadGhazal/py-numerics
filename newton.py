from math import *

def newton(f, fp, x0, tol, m = 1):

    iterate = [x0]

    error = []

    rel_error = [0]

    iterate.append(x0 - ((m * f(x0)) / fp(x0)))

    while True:

        if abs(iterate[-1] - iterate[-2]) < tol:

            break

        iterate.append(iterate[-1] - ((m * f(iterate[-1])) / fp(iterate[-1])))

        print iterate[-1]

    for i in xrange(len(iterate)):

        error.append(abs(iterate[i] - iterate[-1]))

    for i in xrange(1, len(error)):

        if m == 1:

            rel_error.append(error[i] / (error[i - 1] ** 2))

        else:

            rel_error.append(error[i] / error[i - 1])

    return iterate, error, rel_error

iterate, error, rel_error = newton(lambda x: x ** 4 - 12.0 * x ** 2 - 44.0, lambda x: 4.0 * x ** 3 - 24.0 * x, 0.9, 0.5 * (10 ** (-8)))

for i in xrange(len(iterate)):

    print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])
