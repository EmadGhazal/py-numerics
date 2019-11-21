import numpy as np

import numpy.linalg as LA

from math import *

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from mpl_toolkits.mplot3d import Axes3D

from mfourrk import mfourrk as solve

def sim(t, w1, w2):

    x1 = w1[:, 0]

    y1 = w1[:, 1]

    z1 = w1[:, 2]

    x2 = w2[:, 0]

    y2 = w2[:, 1]

    z2 = w2[:, 2]

    fig = plt.figure()

    ax = Axes3D(fig)

    ax.set_xlim3d(-max(max(x1), max(x2)) - 1, max(max(x1), max(x2)) + 1)

    ax.set_ylim3d(-max(max(y1), max(y2)) - 1, max(max(y1), max(y2)) + 1)

    ax.set_zlim3d(-max(max(z1), max(z2)) - 1, max(max(z1), max(z2)) + 1)

    pt1, = ax.plot([], [], [], "bo")

    pa1, = ax.plot([], [], [], "r")

    pt2, = ax.plot([], [], [], "go")

    pa2, = ax.plot([], [], [], "k")

    def animate(i):

        pt1.set_data([x1[i]], [y1[i]])

        pt1.set_3d_properties([z1[i]])

        pa1.set_data(x1[:i], y1[:i])

        pa1.set_3d_properties(z1[:i])

        pt2.set_data([x2[i]], [y2[i]])

        pt2.set_3d_properties([z2[i]])

        pa2.set_data(x2[:i], y2[:i])

        pa2.set_3d_properties(z2[:i])

        return pt1, pa1, pt2, pa2,

    anime = animation.FuncAnimation(fig, animate, frames = t.shape[0], interval = 0, blit = True, repeat = True)

    ax.grid()

    plt.show()

    return None

def main():

    s = 10

    r = 28

    b = 8/3

    y0 = np.array([5, 5, 5])

    f1 = lambda t, y: -s * y[0] + s * y[1]

    f2 = lambda t, y: -y[0] * y[2] + r * y[0] - y[1]

    f3 = lambda t, y: y[0] * y[1] - b * y[2]

    f = lambda t, y: np.array([f1(t, y), f2(t, y), f3(t, y)])

    t, w1 = solve(f, y0, 1000, 20)

    t, w2 = solve(f, y0 + 10 ** -5, 1000, 20)

    sym1 = np.array([])

    sym2 = np.array([])

    ind = np.array([])

    for i in range(t.shape[0]):

        if w1[i, 0] >=0:

            sym1 = np.append(sym1, 1)

        else:

            sym1 = np.append(sym1, 0)

        if w2[i, 0] >=0:

            sym2 = np.append(sym2, 1)

        else:

            sym2 = np.append(sym2, 0)

        if sym1[i] != sym2[i]:

            ind = np.append(ind, i)

    print(sym1, "\n", sym2, "\n", ind)

    print(t[10539])

    print(w1[10539, 0], w2[10539, 0])

    print(sym1[10539], sym2[10539])

    print((LA.norm(abs(w1[10000] - w2[10000])) / LA.norm(w1[10000])) / (10 ** -5 / LA.norm([5, 5, 5])))

    print((LA.norm(abs(w1[19999] - w2[19999])) / LA.norm(w1[19999])) / (10 ** -5 / LA.norm([5, 5, 5])))

    sim(t, w1, w2)

main()
