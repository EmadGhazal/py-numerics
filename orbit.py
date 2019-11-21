import numpy as np

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from fourrk import fourrk as solve

def sim(t, w):

    x1 = w[:, 0]

    y1 = w[:, 2]

    x2 = w[:, 4]

    y2 = w[:, 6]

    #x3 = w[:, 8]

    #y3 = w[:, 10]

    fig, ax = plt.subplots(1, 1)

    ax.set_xlim(-max(max(x1), max(x2)) - 1, max(max(x1), max(x2)) + 1)

    ax.set_ylim(-10 * max(max(y1), max(y2)) - 1, 10 * max(max(y1), max(y2)) + 1)

    ax.plot(x1, y1)

    ax.plot(x2, y2)

    #ax.plot(x3, y3)

    #ax[1].set_xlim(min(t), max(t))

    #ax[1].set_ylim(min(min(r1), min(v1)) - 1, max(max(r1), max(r1)) + 1)

    #ax[2].set_xlim(min(t), max(t))

    #ax[2].set_ylim(min(min(r2), min(v2)) - 1, max(max(r2), max(v2)) + 1)

    #ax[0].plot(x, y, "r")

    #ax[1].plot(t, r1, "b")

    #ax[1].plot(t, v1, "r")

    #ax[2].plot(t, r2, "b")

    #ax[2].plot(t, v2, "r")

    p1, = ax.plot([], [], "bo")

    p2, = ax.plot([], [], "ro")

    #p3, = ax.plot([], [], "ko")

    #pv1, = ax[1].plot([], [], "go")

    #pr2, = ax[2].plot([], [], "ko")

    #pv2, = ax[2].plot([], [], "go")

    def animate(i):

        p1.set_data(x1[i], y1[i])

        p2.set_data(x2[i], y2[i])

        #p3.set_data(x3[i], y3[i])

        #pv1.set_data(t[i], v1[i])

        #pr2.set_data(t[i], r2[i])

        #pv2.set_data(t[i], v2[i])

        return p1, p2,

    anime = animation.FuncAnimation(fig, animate, frames = t.shape[0], interval = 0, blit = True, repeat = True)

    ax.grid()

    #ax[1].grid()

    #ax[2].grid()

    plt.show()

    return None

def main():

    G = 1

    m1 = 0.3

    m2 = 0.03

    m3 = 0

    y02 = np.array([2, 0.2, 2, -0.2, 0, -0.01, 0, 0.01])

    f2 = lambda t, y: np.array([y[1],

                               (G * m2 * (y[4] - y[0])) / (((y[4] - y[0]) ** 2 + (y[6] - y[2]) ** 2) ** (3/2)),

                               y[3],

                               (G * m2 * (y[6] - y[2])) / (((y[4] - y[0]) ** 2 + (y[6] - y[2]) ** 2) ** (3/2)),

                               y[5],

                               (G * m1 * (y[0] - y[4])) / (((y[0] - y[4]) ** 2 + (y[2] - y[6]) ** 2) ** (3/2)),

                               y[7],

                               (G * m1 * (y[2] - y[6])) / (((y[0] - y[4]) ** 2 + (y[2] - y[6]) ** 2) ** (3/2))])

    y03 = np.array([2, 0.2, 2, -0.2, 0, -0.01, 0, 0.01, -2, -0.2, -2, 0.2])

    f3 = lambda t, y: np.array([y[1],

                               (G * m2 * (y[4] - y[0])) / (((y[4] - y[0]) ** 2 + (y[6] - y[2]) ** 2) ** (3/2)) +

                               (G * m3 * (y[8] - y[0])) / (((y[8] - y[0]) ** 2 + (y[10] - y[2]) ** 2) ** (3/2)),

                               y[3],

                               (G * m2 * (y[6] - y[2])) / (((y[4] - y[0]) ** 2 + (y[6] - y[2]) ** 2) ** (3/2)) +

                               (G * m3 * (y[10] - y[2])) / (((y[8] - y[0]) ** 2 + (y[10] - y[2]) ** 2) ** (3/2)),

                               y[5],

                               (G * m1 * (y[0] - y[4])) / (((y[0] - y[4]) ** 2 + (y[2] - y[6]) ** 2) ** (3/2)) +

                               (G * m3 * (y[8] - y[4])) / (((y[8] - y[4]) ** 2 + (y[10] - y[6]) ** 2) ** (3/2)),

                               y[7],

                               (G * m1 * (y[2] - y[6])) / (((y[0] - y[4]) ** 2 + (y[2] - y[6]) ** 2) ** (3/2)) +

                               (G * m3 * (y[10] - y[6])) / (((y[8] - y[4]) ** 2 + (y[10] - y[6]) ** 2) ** (3/2)),

                               y[9],

                               (G * m1 * (y[0] - y[8])) / (((y[0] - y[8]) ** 2 + (y[2] - y[10]) ** 2) ** (3/2)) +

                               (G * m2 * (y[4] - y[8])) / (((y[4] - y[8]) ** 2 + (y[6] - y[10]) ** 2) ** (3/2)),

                               y[11],

                               (G * m1 * (y[2] - y[10])) / (((y[0] - y[8]) ** 2 + (y[2] - y[10]) ** 2) ** (3/2)) +

                               (G * m2 * (y[6] - y[10])) / (((y[4] - y[8]) ** 2 + (y[6] - y[10]) ** 2) ** (3/2))])

    t, w = solve(f2, y02, 100, 100)

    sim(t, w)

main()
