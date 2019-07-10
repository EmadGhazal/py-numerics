from math import *

def iqi(f, x0, x1, x2, tol):

    iterate = [x0, x1, x2]

    error = []

    rel_error = [0]

    q = lambda x, y: f(x) / f(y)

    x, y, z = iterate[-3], iterate[-2], iterate[-1]

    iterate.append(z - (q(z, y) * (q(z, y) - q(x, y)) * (z - y)  + (1.0 - q(z, y)) * q(z, x) * (z - x)) / ((q(x, y) - 1.0) * (q(z, y) - 1.0) * (q(z, x) - 1.0)))

    while True:

        if abs(iterate[-1] - iterate[-2]) < tol:

            break

        x, y, z = iterate[-3], iterate[-2], iterate[-1]

        iterate.append(z - (q(z, y) * (q(z, y) - q(x, y)) * (z - y)  + (1.0 - q(z, y)) * q(z, x) * (z - x)) / ((q(x, y) - 1.0) * (q(z, y) - 1.0) * (q(z, x) - 1.0)))

    for i in xrange(len(iterate)):

        error.append(abs(iterate[i] - iterate[-1]))

    for i in xrange(1, len(error)):

            rel_error.append(error[i] / (error[i - 1] ** ((1.0 + sqrt(5)) / 2.0)))

    return iterate, error, rel_error

iterate, error, rel_error = iqi(lambda x: exp(x) + sin(x) - 4.0, 1.0, 2.0, 0.0, 0.5 * (10 ** (-8)))

for i in xrange(len(iterate)):

    print "{:19.16f}    {:19.16f}   {:19.16f}".format(iterate[i], error[i], rel_error[i])
