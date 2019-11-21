from math import *

a = lambda x: (1.0 - (1.0 / cos(x))) / (tan(x) ** 2)

b = lambda x: (1.0 - (1.0 - x) ** 3) / x

ap = lambda x: -1.0 / (1.0 + (1.0 / cos(x)))

bp = lambda x: 3.0 - 3.0 * x + x ** 2

al = []

bl = []

apl = []

bpl = []

for i in xrange(1, 15):

    al.append(a(10 ** -i))

    apl.append(ap(10 ** -i))

    bl.append(b(10 ** -i))

    bpl.append(bp(10 ** -i))

for i in xrange(len(al)):

    print "{:19.16f}    {:19.16f}   {:19.16f}   {:19.16f}".format(al[i], apl[i], bl[i], bpl[i])
