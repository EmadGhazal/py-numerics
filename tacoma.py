import numpy as np

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from mfourrk import mfourrk as solve

import numba

solve = numba.jit(nopython = True)(solve)

m = 2500

k = 1000

l = 6

d = 0.01

a = 0.2

om = 2 * pi * (38 / 60)

W = 80 #58.98674309

def sim(t, w):

    y = w[:, 0]

    v = w[:, 1]

    th = w[:, 2]

    w = w[:, 3]

    fig, ax = plt.subplots(3, 1)

    ax[0].set_xlim(-(max(abs(min(y)), abs(max(y)))) - 1, (max(abs(min(y)), abs(max(y)))) + 1)

    ax[0].set_ylim(-(max(abs(min(y)), abs(max(y)))) - 1, (max(abs(min(y)), abs(max(y)))) + 1)

    ax[0].set_aspect("equal")

    ax[1].plot(t, y, label = "y")

    ax[1].plot(t, v, label = "v")

    ax[2].plot(t, th, label = "th")

    ax[2].plot(t, w, label = "w")

    br, = ax[0].plot([], [], "r")

    title = ax[0].text(0, (max(abs(min(y)), abs(max(y)))), "")

    def animate(i):

        mx = 0

        my = -y[i]

        rx = l * cos(th[i])

        ry = -(y[i] - l * sin(th[i]))

        lx = -l * cos(th[i])

        ly = -(y[i] + l * sin(th[i]))

        br.set_data([lx, mx, rx], [ly, my, ry])

        title.set_text(str(t[i]))

        return br, title,

    anime = animation.FuncAnimation(fig, animate, frames = np.arange(0, t.shape[0], 25), interval = 0, blit = True, repeat = True)

    ax[0].grid()

    ax[1].grid()

    ax[2].grid()

    plt.legend()

    plt.show()

    return None

@numba.jit(nopython = True)

def f1(t, y):

    return y[1]

@numba.jit(nopython = True)

def f2(t, y):

    return -d * y[1] - k / (m * a) * (exp(a * (y[0] - l * sin(y[2]))) + exp(a * (y[0] + l * sin(y[2]))) - 2) + 0.2 * W * sin(om * t)

@numba.jit(nopython = True)

def f3(t, y):

    return y[3]

@numba.jit(nopython = True)

def f4(t, y):

    return -d * y[3] + 3 * cos(y[2]) * k / (l * m * a) * (exp(a * (y[0] - l * sin(y[2]))) - exp(a * (y[0] + l * sin(y[2]))))

@numba.jit(nopython = True)

def f(t, y):

    return np.array([f1(t, y), f2(t, y), f3(t, y), f4(t, y)])

def main():

    y0 = np.array([0, 0, 10 ** -3, 0])

    t, w = solve(f, y0, 5000, 1000)

    print(max(abs(w[:, 2])))

    sim(t, w)

main()
