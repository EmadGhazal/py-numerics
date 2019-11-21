import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from asimp import asimp as intg

from math import *

from newton import newton as solve

x = lambda t: 1 + 6 * t ** 2 - 5 * t ** 3

y = lambda t: 1 + 6 * t - 6 * t ** 2 + t ** 3

f = lambda t: sqrt((12 * t - 15 * t ** 2) ** 2 + (6 - 12 * t + 3 * t ** 2) ** 2)

def sim(t, xp, yp, xpp = None, ypp = None):

    fig, ax = plt.subplots()

    point, = plt.plot([x(0)], [y(0)], "ro")

    def animate(i):

        point.set_data(x(i), y(i))

        return point,

    l = plt.plot(xp, yp)

    #if xpp is None:

        #plt.plot(xp, yp, "ko")

    #else:

        #plt.plot(xpp, ypp, "ko")

    ax = plt.axis([min(xp) - 0.1, max(xp) + 0.1, min(yp) - 0.1, max(yp) + 0.1])

    anime = animation.FuncAnimation(fig, animate, frames = t, interval = 50, blit = True, repeat = True)

    plt.grid()

    plt.show()

    return None

def arc(t):

    return intg(f, 0, t, 0.5 * 10 ** -6)[0]

def part(s, a):

    g = lambda x: arc(x) - s * arc(1)

    return solve(g, f, a, 0.5 * 10 ** -6)

def partn(n):

    C = lambda s: s

    t = np.array([0, 1], np.float)

    if n == 1:

        return t

    for i in range(1, n):

        t = np.insert(t, i, part(C(i / n), t[i - 1]))

    return t

def main():

    t = np.linspace(0, 1, 100)

    xp = np.vectorize(x)

    yp = np.vectorize(y)

    xpp = xp(t)

    ypp = yp(t)

    sim(t, xpp, ypp)

    t = partn(99)

    xppp = xp(t)

    yppp = yp(t)

    sim(t, xpp, ypp, xppp, yppp)

main()
