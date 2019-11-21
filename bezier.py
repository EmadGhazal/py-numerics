import numpy as np

from nestm import nestm

import matplotlib.pyplot as plt

def bezier(x, y, z):

    bx = 3.0 * (x[1] - x[0])

    cx = 3.0 * (x[2] - x[1]) - bx

    dx = x[3] - x[0] - bx - cx

    by = 3.0 * (y[1] - y[0])

    cy = 3.0 * (y[2] - y[1]) - by

    dy = y[3] - y[0] - by - cy

    bz = 3.0 * (z[1] - z[0])

    cz = 3.0 * (z[2] - z[1]) - bz

    dz = z[3] - z[0] - bz - cz

    xt = np.array([x[0], bx, cx, dx])

    yt = np.array([y[0], by, cy, dy])

    zt = np.array([z[0], bz, cz, dz])

    return xt, yt, zt

def plotp(xt, yt, zt, x, y, z):

    t = np.linspace(0, 1, 100)

    b = np.array([])

    xp = nestm(xt, b, t)

    yp = nestm(yt, b, t)

    plt.plot(xp, yp, "r")

    #plt.plot([x[0], x[1]], [y[0], y[1]], ":k")

    #plt.plot([x[2], x[3]], [y[2], y[3]], ":k")

    #plt.plot(x[0], y[0], "ob", x[1], y[1], "ob", x[2], y[2], "ob", x[3], y[3], "ob")

    #plt.grid()

    #plt.show()

    return None

x = ["289 452 289 452 166 452 166 452", "166 452 166 452 166 568 166 568", "166 568 166 627 185 657 223 657", "223 657 245 657 258 647 276 618",
     "276 618 292 589 304 580 321 580", "321 580 345 580 363 598 363 621", "363 621 363 657 319 683 259 683", "259 683 196 683 144 656 118 611",
     "118 611 92 566 84 530 83 450", "83 450 83 450 1 450 1 450", "1 450 1 450 1 418 1 418", "1 418 1 418 83 418 83 418", "83 418 83 418 83 104 83 104",
     "83 104 83 31 72 19 0 15", "0 15 0 15 0 0 0 0", "0 0 0 0 260 0 260 0", "260 0 260 0 260 15 260 15", "260 15 178 18 167 29 167 104",
     "167 104 167 104 167 418 167 418", "167 418 167 418 289 418 289 418", "289 418 289 418 289 452 289 452"]

y = []

xp = []

yp = []

xpp = []

ypp = []

for element in x:

    y.append(element.split())

for element in y:

    for i in range(len(element)):

        if i % 2 == 0:

            xp.append(element[i])

        else:

            yp.append(element[i])

for i in range(len(xp)):

    xp[i] = float(xp[i])

    yp[i] = float(yp[i])

for i in range(0, len(xp), 4):

    xpp.append(xp[i:i + 4])

    ypp.append(yp[i:i+4])

xpp = np.array(xpp)

ypp = np.array(ypp)

zpp = np.zeros((21, 4))

for i in range(xpp.shape[0]):

    xt, yt, zt = bezier(xpp[i], ypp[i], zpp[i])

    plotp(xt, yt, zt, xpp, ypp, zpp)

plt.grid()

plt.show()

"""x = np.array([1.0, 1.0, 1.0, 1.0])

y = np.array([1.0, 1.0, 5.0, 5.0])

z = np.array([0.0, 0.0, 0.0, 0.0])

xt, yt, zt = bezier(x, y, z)

plotp(xt, yt, zt, x, y, z)

x = np.array([1.0, 5.0, 5.0, 1.0])

y = np.array([5.0, 5.0, 1.0, 1.0])

z = np.array([0.0, 0.0, 0.0, 0.0])

xt, yt, zt = bezier(x, y, z)

plotp(xt, yt, zt, x, y, z)

plt.grid()

plt.show()
"""
