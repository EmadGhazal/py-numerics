from math import *

from scipy.optimize import fsolve

def f(x):

    return (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) * (x - 6) * (x - 7) * (x - 8) * (x - 9) * (x - 10) * (x - 11) * (x - 12) * (x - 13) * (x - 14) * (x - 15) * (x - 16) * (x - 17) * (x - 18) * (x - 19) * (x - 20) - 2 * (10 ** -15) * (x ** 15)

xa = fsolve(f, 15)[0]

print "{:19.16f}    {:19.16f}".format(xa, f(xa))
