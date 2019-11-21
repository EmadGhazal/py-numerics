import numpy as np

def nestm(c, b, x):

    d = c.size

    if b.size == 0:

        b = np.zeros(d)

    y = c[d - 1]

    for i in range(d - 2, -1, -1):

        y = c[i] + (x - b[i]) * y

    return y
