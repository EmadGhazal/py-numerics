from math import log, pi, cos, sqrt, exp, sin

def simp(f, a, b, m):

    h = (b - a) / (2 * m)

    ap = a + h

    sig1 = 0

    sig2 = f(a + h)

    for i in range(1, m):

        sig1 = sig1 + f(a + i * 2 * h)

    for i in range(2, m + 1):

        sig2 = sig2 + f(ap + (i - 1) * 2 * h)

    return h / 3 * (f(a) + f(b) + 4 * sig2 + 2 * sig1), (b - a) * h ** 4 / 180

def main():

    f = lambda x: sqrt(1 + (1 / cos(x)) ** 4)

    for element in [32]:

        print(simp(f, 0, pi/4, element))

        #print(simp(f, 0, 1, element)[0] - log(sqrt(2) + 1)/2)

main()
