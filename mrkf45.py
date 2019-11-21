import numpy as np

from math import *

import numpy.linalg as LA

def mrkf45(f, y0, b, tol):

    w = [y0]

    t = [0]

    h = [0.1]

    flag = 1

    while True:

        hi = h[-1]

        ti = t[-1]

        wi = w[-1]

        if ti > b:

            hi = b - t[-2]

            t.pop()

            w.pop()

            ti = t[-1]

            wi = w[-1]

            flag = 0

        s1 = f(ti, wi)

        s2 = f(ti + 1/4 * hi, wi + 1/4 * hi * s1)

        s3 = f(ti + 3/8 * hi, wi + 3/32 * hi * s1 + 9/32 * hi * s2)

        s4 = f(ti + 12/13 * hi, wi + 1932/2197 * hi * s1 - 7200/2197 * hi * s2 + 7296/2197 * hi * s3)

        s5 = f(ti + hi, wi + 439/216 * hi * s1 - 8 * hi * s2 + 3680/513 * hi * s3 - 845/4104 * hi * s4)

        s6 = f(ti + 1/2 * hi, wi - 8/27 * hi * s1 + 2 * hi * s2 - 3544/2565 * hi * s3 + 1859/4104 * hi * s4 - 11/40 * hi * s5)

        wi1 = wi + hi * (25/216 * s1 + 1408/2565 * s3 + 2197/4104 * s4 - 1/5 * s5)

        zi1 = wi + hi * (16/135 * s1 + 6656/12825 * s3 + 28561/56430 * s4 - 9/50 * s5 + 2/55 * s6)

        ei = LA.norm(wi1 - zi1)

        eri = ei / LA.norm(wi1)

        if eri < tol:

            w.append(zi1)

            if ei == 0:

                h.append(0.1)

            else:

                h.append(0.8 * hi * ((tol * LA.norm(wi1) / ei) ** (1 / 5)))

        else:

            h[-1] = 0.8 * hi * ((tol * LA.norm(wi1) / ei) ** (1 / 5))

            continue

        t.append(ti + hi)

        if flag == 0:

            break

    h = h[:-3]

    h.append(hi)

    return h, t, w

def main():

    f = lambda t, y: np.array([y[0] + y[1], -y[0] + y[1]])

    fp = lambda t: np.array([exp(t) * cos(t), -exp(t) * sin(t)])

    h, t, w = mrkf45(f, np.array([1, 0]), 1, 0.5 * 10 ** -8)

    sol = []

    for elm in t:

        sol.append(fp(elm))

    h, t, w, sol = np.array(h), np.array(t), np.array(w), np.array(sol)

    print(h, "\n")

    print(t, "\n")

    print(w, "\n")

    print(sol, "\n")

    print(max(h))

    print(len(h))

    print(LA.norm(w - sol) / LA.norm(w))

main()
