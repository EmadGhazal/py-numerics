import numpy as np

def nestm(c, b, x):

    c = (np.array(c)).astype(float)

    b = (np.array(b)).astype(float)

    x = float(x)

    d = c.size

    if b.size == 0:

        b = np.zeros(d - 1)

    y = c[d - 1]

    for i in xrange(d - 2, -1, -1):

        y = c[i] + (x - b[i]) * y

    return y
