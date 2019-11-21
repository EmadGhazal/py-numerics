from math import *

def fpi(f, x0, tol):

    if f(x0) == 0:

        return x0

    root = []

    error = []

    error_rel = []

    root.append(f(x0))

    while True:

        print(root[-1])

        root.append(f(root[-1]))

        error.append(abs(root[-1] - root[-2]))

        if error[-1] < tol:

            break

    for i in range(1, len(error)):

        error_rel.append(error[i] / error[i - 1])

    return root[-1], error_rel[-1]

print(fpi(lambda x: 6 / tan(x), pi, 0.5 * (10 ** (-6))))
