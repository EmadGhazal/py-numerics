from math import *

import numpy as np

from numpy import linalg as LA

import matplotlib.pyplot as plt

from jacobi import jacobi

g = 9.81

L = 2.0

w = 0.3

t = 0.03

rho = 480.0

p = 100

E = 1.3 * 10 ** 10

I = w * t ** 3 / 12.0

def step(x, a):

    if x - a < 0.0:

        return 0.0

    else:

        return 1.0

nl = -rho * w * t * g

s = lambda x: -p * g * sin(pi / L * x)

d = lambda x: -step(x, 1.8) * 350 * g

#yx = lambda x: (nl / (24.0 * E * I)) * x ** 2 * (x ** 2 - 4.0 * L * x + 6.0 * L ** 2) \
#     - (p * g * L / (E * I * pi)) * (L ** 3 / pi ** 3 * sin(pi / L * x) - x ** 3 / 6.0 + L / 2.0 * x ** 2 - L ** 2 / pi ** 2 * x)

def cstruc(n):

    A = np.zeros((n, n))

    A[0][0], A[0][1], A[0][2], A[0][3] = 16.0, -9.0, 8.0 / 3.0, -1.0 / 4.0

    A[1][0], A[1][1], A[1][2], A[1][3] = -4.0, 6.0, -4.0, 1.0

    A[n - 2][n - 4], A[n - 2][n - 3], A[n - 2][n - 2], A[n - 2][n - 1] = 16.0 / 17.0, -60.0 / 17.0, 72.0 / 17.0, -28.0 / 17.0

    A[n - 1][n - 4], A[n - 1][n - 3], A[n - 1][n - 2], A[n - 1][n - 1] = -12.0 / 17.0, 96.0 / 17.0, -156.0 / 17.0, 72.0 / 17.0

    for i in range(2, n - 2):

        A[i][i - 2], A[i][i - 1], A[i][i], A[i][i + 1], A[i][i + 2] = 1.0, -4.0, 6.0, -4.0, 1.0

    return A

def ccstruc(n):

    A = np.zeros((n, n))

    A[0][0], A[0][1], A[0][2], A[0][3] = 16.0, -9.0, 8.0 / 3.0, -1.0 / 4.0

    A[1][0], A[1][1], A[1][2], A[1][3] = -4.0, 6.0, -4.0, 1.0

    A[n - 2][n - 4], A[n - 2][n - 3], A[n - 2][n - 2], A[n - 2][n - 1] = 1.0, -4.0, 6.0, -4.0

    A[n - 1][n - 4], A[n - 1][n - 3], A[n - 1][n - 2], A[n - 1][n - 1] = -1.0 / 4.0, 8.0 / 3.0, -9.0, 16.0

    for i in range(2, n - 2):

        A[i][i - 2], A[i][i - 1], A[i][i], A[i][i + 1], A[i][i + 2] = 1.0, -4.0, 6.0, -4.0, 1.0

    return A

def load(n):

    h = L / n

    x = np.zeros(n)

    b = np.zeros(n)

    for i in range(n):

        x[i] = (i + 1) * h

        b[i] = h ** 4 * (nl + s(x[i])) / (E * I)

    return x, b

def deflect(n):

    x, b = load(n)

    A = cstruc(n)

    print(A)

    ya, itr = jacobi(A, b, np.zeros(n))

    #yxv = np.vectorize(yx)

    #ye = yxv(x)

    #con = LA.cond(A, np.inf)

    return x, ya

for i in range(1, 12):

    n = 10 * 2 ** i

    x, ya = deflect(n)

    #print("{:19.16f}".format(ya[n - 1]))

    x = np.insert(x, 0, 0.0)

    ya = np.insert(ya, 0, 0.0)

    #ye = np.insert(ye, 0, 0.0)

    plt.plot(x, ya, "r")

    #plt.plot(x, ye, "b")

    plt.ylim(-0.5, 0.5)

    plt.grid()

    plt.show()
