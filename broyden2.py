import numpy as np

import numpy.linalg as LA

F1 = lambda x: (x[0] - 1.0) ** 2 + x[1] ** 2 + (x[2] - 1.0) ** 2 - 8.0

F2 = lambda x: x[0] ** 2 + (x[1] - 2.0) ** 2 + (x[2] - 2.0) ** 2 - 2.0

F3 = lambda x: x[0] ** 2 + (x[1] - 3.0) ** 2 + (x[2] - 3.0) ** 2 - 2.0

def broyden2(x0, A0):

    xp = np.copy(x0)

    Ap = np.copy(A0)

    itr = 0

    while True:

        print(xp)

        x = np.copy(xp)

        A = np.copy(Ap)

        F = np.array([F1(x), F2(x), F3(x)])

        xp = x - np.dot(A, F)

        if LA.norm(xp - x, np.inf) < 0.5 * 10 ** -6:

            break

        Fp = np.array([F1(xp), F2(xp), F3(xp)])

        d = xp - x

        D = Fp - F

        Ap = A + np.dot(np.dot(d - np.dot(A, D), np.transpose(d)), A) / np.dot(np.dot(np.transpose(d), A), D)

        itr += 1

    return xp, itr

print(broyden2(np.array([[0.0], [0.0], [0.0]]), np.identity(3)))
