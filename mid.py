from math import log, pi, cos, sqrt, exp, sin, atan

def mid(f, a, b, m):

    h = (b - a) / m

    ap = a + h / 2

    sig = f(ap)

    for i in range(2, m + 1):

        sig = sig + f(ap + (i - 1) * h)

    return h * sig, (b - a) * h ** 2 / 24

def main():

    f = lambda x: atan(x) / x

    for element in [16, 32]:

        print(mid(f, 0, 1, element))

        #print(mid(f, 0, pi/2, element)[0] - 2 * sqrt(2))

main()
