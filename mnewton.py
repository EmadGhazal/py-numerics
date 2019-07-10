import numpy as np

import numpy.linalg as LA

from gaussp import gaussp as gauss

F1 = lambda x: (x[0] - 1.0) ** 2 + x[1] ** 2 + (x[2] - 1.0) ** 2 - 8.0

F2 = lambda x: x[0] ** 2 + (x[1] - 2.0) ** 2 + (x[2] - 2.0) ** 2 - 2.0

F3 = lambda x: x[0] ** 2 + (x[1] - 3.0) ** 2 + (x[2] - 3.0) ** 2 - 2.0

J11 = lambda x: 2.0 * (x[0] - 1.0)

J12 = lambda x: 2.0 * x[1]

J13 = lambda x: 2.0 * (x[2] - 1.0)

J21 = lambda x: 2.0 * x[0]

J22 = lambda x: 2.0 * (x[1] - 2.0)

J23 = lambda x: 2.0 * (x[2] - 2.0)

J31 = lambda x: 2.0 * x[0]

J32 = lambda x: 2.0 * (x[1] - 3.0)

J33 = lambda x: 2.0 * (x[2] - 3.0)

def mnewton(x0):

    xp = np.copy(x0)

    while True:

        print(xp)

        x = np.copy(xp)

        J = np.array([[J11(x), J12(x), J13(x)], [J21(x), J22(x), J23(x)], [J31(x), J32(x), J33(x)]])

        F = np.array([F1(x), F2(x), F3(x)])

        s = gauss(J, -F)

        xp = x + s

        if LA.norm(xp - x, np.inf) < 0.5 * 10 ** -6:

            break

    return xp

mnewton(np.array([[1.0], [1.0], [1.0]]))
