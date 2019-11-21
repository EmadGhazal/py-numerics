import numpy as np

import numpy.linalg as LA

from gaussp import gaussp as gauss

A1, B1, C1 = 15600, 7540, 20140

A2, B2, C2 = 18760, 2750, 18610

A3, B3, C3 = 17610, 14630, 13480

A4, B4, C4 = 19170, 610, 18390

t1, t2, t3, t4 = 0.07074, 0.07220, 0.07690, 0.07242

c = 299792.458

F1 = lambda x: (x[0, 0] - A1) ** 2 + (x[1, 0] - B1) ** 2 + (x[2, 0] - C1) ** 2 - (c * (t1 - x[3, 0])) ** 2

F2 = lambda x: (x[0, 0] - A2) ** 2 + (x[1, 0] - B2) ** 2 + (x[2, 0] - C2) ** 2 - (c * (t2 - x[3, 0])) ** 2

F3 = lambda x: (x[0, 0] - A3) ** 2 + (x[1, 0] - B3) ** 2 + (x[2, 0] - C3) ** 2 - (c * (t3 - x[3, 0])) ** 2

F4 = lambda x: (x[0, 0] - A4) ** 2 + (x[1, 0] - B4) ** 2 + (x[2, 0] - C4) ** 2 - (c * (t4 - x[3, 0])) ** 2

J11 = lambda x: 2 * (x[0, 0] - A1)

J12 = lambda x: 2 * (x[1, 0] - B1)

J13 = lambda x: 2 * (x[2, 0] - C1)

J14 = lambda x: 2 * c ** 2 * (t1 - x[3, 0])

J21 = lambda x: 2 * (x[0, 0] - A2)

J22 = lambda x: 2 * (x[1, 0] - B2)

J23 = lambda x: 2 * (x[2, 0] - C2)

J24 = lambda x: 2 * c ** 2 * (t2 - x[3, 0])

J31 = lambda x: 2 * (x[0, 0] - A3)

J32 = lambda x: 2 * (x[1, 0] - B3)

J33 = lambda x: 2 * (x[2, 0] - C3)

J34 = lambda x: 2 * c ** 2 * (t3 - x[3, 0])

J41 = lambda x: 2 * (x[0, 0] - A4)

J42 = lambda x: 2 * (x[1, 0] - B4)

J43 = lambda x: 2 * (x[2, 0] - C4)

J44 = lambda x: 2 * c ** 2 * (t4 - x[3, 0])

def mnewton(x0):

    xp = np.copy(x0)

    while True:

        print(xp)

        x = np.copy(xp)

        J = np.array([[J11(x), J12(x), J13(x), J14(x)], [J21(x), J22(x), J23(x), J24(x)], [J31(x), J32(x), J33(x), J34(x)], [J41(x), J42(x), J43(x), J44(x)]])

        F = np.array([[F1(x)], [F2(x)], [F3(x)], [F4(x)]])

        s = gauss(J, -F)

        xp = x + s

        if LA.norm(s, np.inf) < 0.5 * 10 ** -6:

            break

    return xp

print(mnewton(np.array([[0.0], [0.0], [6370.0], [0.0]])))
