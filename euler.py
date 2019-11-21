import numpy as np

from math import *

import matplotlib.pyplot as plt

def euler(f, y0, n, b):

    w = np.array([y0])

    t = np.array([0])

    h = 1 / n

    for i in range(0, int(b * n)):

        w = np.append(w, w[-1] + h * f(t[-1], w[-1]))

        t = np.append(t, t[-1] + h)

    return t, w

def main():

    t, w = euler(lambda t, y: t * y + t ** 3, 1, 5, 1)

    print(t)

    print(w)

#main()
