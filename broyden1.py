import numpy as np

import numpy.linalg as LA

from gaussp import gaussp as gauss

from math import sqrt

A1, B1, C1 = 15600, 7540, 20140

A2, B2, C2 = 18760, 2750, 18610

A3, B3, C3 = 17610, 14630, 13480

A4, B4, C4 = 19710, 610, 18390

t1, t2, t3, t4 = 0.07074, 0.07220, 0.07690, 0.07242

c = 299792.458

F1 = lambda x: sqrt((x[0, 0] - A1) ** 2 + (x[1, 0] - B1) ** 2 + (x[2, 0] - C1) ** 2) - c * (t1 - x[3, 0])

F2 = lambda x: sqrt((x[0, 0] - A2) ** 2 + (x[1, 0] - B2) ** 2 + (x[2, 0] - C2) ** 2) - c * (t2 - x[3, 0])

F3 = lambda x: sqrt((x[0, 0] - A3) ** 2 + (x[1, 0] - B3) ** 2 + (x[2, 0] - C3) ** 2) - c * (t3 - x[3, 0])

F4 = lambda x: sqrt((x[0, 0] - A4) ** 2 + (x[1, 0] - B4) ** 2 + (x[2, 0] - C4) ** 2) - c * (t4 - x[3, 0])

def broyden1(x0, A0):

    xp = np.copy(x0)

    Ap = np.copy(A0)

    itr = 0

    while True:

        print(xp)

        x = np.copy(xp)

        A = np.copy(Ap)

        F = np.array([[F1(x)], [F2(x)], [F3(x)], [F4(x)]])

        s = LA.solve(A, -F)

        xp = x + s

        if LA.norm(s, np.inf) < 0.5 * 10 ** -3:

            break

        Fp = np.array([[F1(xp)], [F2(xp)], [F3(xp)], [F4(xp)]])

        d = xp - x

        D = Fp - F

        Ap = A + np.dot(D - np.dot(A, d), np.transpose(d)) / np.dot(np.transpose(d), d)

        itr += 1

    return xp, itr

print(broyden1(np.array([[0.0], [0.0], [6370.0], [0.0]]), np.identity(4)))
