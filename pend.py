import numpy as np

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from mrkf45 import mrkf45 as solve

def sim(t, w, x, y, xp, yp):

    fig, ax = plt.subplots(3, 1)

    ax[0].set_xlim(-3, 3)

    ax[0].set_ylim(-3, 3)

    ax[0].set_aspect("equal")

    ax[1].set_xlim(min(t), max(t))

    ax[1].set_ylim(min(min(w[:, 0]), min(w[:, 2])) - 1, max(max(w[:, 0]), max(w[:, 2])) + 1)

    ax[2].set_xlim(min(t), max(t))

    ax[2].set_ylim(min(min(w[:, 1]), min(w[:, 3])) - 1, max(max(w[:, 1]), max(w[:, 3])) + 1)

    ax[1].plot(t, w[:, 0], "r")

    ax[1].plot(t, w[:, 2], "c")

    ax[2].plot(t, w[:, 1], "r")

    ax[2].plot(t, w[:, 3], "c")

    bob1, = ax[0].plot([], [], "bo")

    rod1, = ax[0].plot([], [], "b")

    bob2, = ax[0].plot([], [], "bo")

    rod2, = ax[0].plot([], [], "b")

    angle1, = ax[1].plot([], [], "bo")

    speed1, = ax[2].plot([], [], "bo")

    angle2, = ax[1].plot([], [], "ko")

    speed2, = ax[2].plot([], [], "bo")

    def animate(i):

        bob1.set_data(x[i], y[i])

        rod1.set_data([0, x[i]], [0, y[i]])

        bob2.set_data(xp[i], yp[i])

        rod2.set_data([x[i], xp[i]], [y[i], yp[i]])

        angle1.set_data(t[i], w[i, 0])

        speed1.set_data(t[i], w[i, 1])

        angle2.set_data(t[i], w[i, 2])

        speed2.set_data(t[i], w[i, 3])

        return bob1, rod1, bob2, rod2, angle1, speed1, angle2, speed2,

    anime = animation.FuncAnimation(fig, animate, frames = x.shape[0], interval = 20, blit = True, repeat = True)

    ax[0].grid()

    ax[1].grid()

    ax[2].grid()

    plt.show()

    return None

def main():

    g = 9.81

    d = 0.1

    y0 = np.array([pi, 0, pi/2, 0])

    f = lambda t, y: np.array([y[1], (-3 * g * sin(y[0])  - g * sin(y[0] - 2 * y[2]) - 2 * sin(y[0] - y[2]) * (y[3] ** 2 - y[1] ** 2 * cos(y[0] - y[2]))) /
                               (3 - cos(2 * y[0] - 2 * y[2])) - d * y[1], y[3], (2 * sin(y[0] - y[2]) * (2 * y[1] ** 2 + 2 * g * cos(y[0]) + y[3] ** 2 * cos(y[0] - y[2]))) /
                               (3 - cos(2 * y[0] - 2 * y[2]))])

    #y = lambda t: np.array([3 * exp(-t) + 2 * exp(4 * t), -2 * exp(-t) + 2 * exp(4 * t)])

    h, t, w = solve(f, y0, 1000, 0.5 * 10 ** -6)

    h, t, w = np.array(h), np.array(t), np.array(w)

    x1 = np.sin(w[:, 0])

    y1 = -np.cos(w[:, 0])

    x2 = np.sin(w[:, 0]) + np.sin(w[:, 2])

    y2 = -(np.cos(w[:, 0]) + np.cos(w[:, 2]))

    sim(t, w, x1, y1, x2, y2)

main()
