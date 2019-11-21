import numpy as np

from math import *

def rk23(f, y0, b, tol):

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

        s2 = f(ti + hi, wi + hi * s1)

        s3 = f(ti + hi / 2, wi + hi / 2 * (s1 + s2) / 2)

        wi1 = wi + hi * (s1 + s2) / 2

        zi1 = wi + hi * (s1 + s2 + 4 * s3) / 6

        ei = abs(wi1 - zi1)

        eri = ei / abs(wi1)

        if eri < tol:

            w.append(zi1)

            if ei == 0:

                h.append(0.1)

            else:

                h.append(0.8 * hi * ((tol * abs(wi1) / ei) ** (1 / 3)))

        else:

            h[-1] = 0.8 * hi * ((tol * abs(wi1) / ei) ** (1 / 3))

            continue

        t.append(ti + hi)

        if flag == 0:

            break

    h = h[:-3]

    h.append(hi)

    return h, t, w

def main():

    #f = lambda t, y: t

    #f = lambda t, y: t ** 2 * y

    #f = lambda t, y: 2 * (t + 1) * y

    #f = lambda t, y: 5 * t ** 4 * y

    #f = lambda t, y: 1 / y ** 2

    f = lambda t, y: t ** 3 / y ** 2

    #fp = lambda t: 1 + t ** 2 / 2

    #fp = lambda t: exp(t ** 3 / 3)

    #fp = lambda t: exp(t ** 2 + 2 * t)

    #fp = lambda t: exp(t ** 5)

    #fp = lambda t: (3 * t + 1) ** (1 / 3)

    fp = lambda t: (3/4 * t ** 4 + 1) ** (1 / 3)

    h, t, w = rk23(f, 1, 1, 0.5 * 10 ** -8)

    h, t, w = np.array(h), np.array(t), np.array(w)

    fp = np.vectorize(fp)

    print(h, "\n")

    print(t, "\n")

    print(w, "\n")

    print(fp(t))

    print(max(h))

    print(len(h))

    print(max(abs(fp(t) - w)))

main()
