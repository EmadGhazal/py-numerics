import numpy as np

from io import StringIO

import sys

def lu(A, b):

    n = A.shape[0]

    l = np.identity(n)

    for j in xrange(n - 1):

        if abs(A[j][j]) == 0:

            print "Error: zero pivot encountered."

            sys.exit()

        for i in xrange(j + 1, n):

            mult = A[i][j] / A[j][j]

            l[i][j] = mult

            for k in xrange(j + 1, n):

                A[i][k] = A[i][k] - mult * A[j][k]

    u = np.triu(A)

    x = np.copy(b)

    for i in xrange(0, n):

        for j in xrange(0, i):

            x[i] = x[i] - l[i][j] * x[j]

        x[i] = x[i] / l[i][i]

    for i in xrange(n - 1, -1, -1):

        for j in xrange(i + 1, n):

            x[i] = x[i] - u[i][j] * x[j]

        x[i] = x[i] / u[i][i]

    return l, u, x

A_in = """
            """

b_in= """
        """

A = np.genfromtxt(StringIO(unicode(A_in)), delimiter = " ")

b = np.genfromtxt(StringIO(unicode(b_in)), delimiter = " ")

l, u, x = lu(A, b)

print l, "\n"

print u, "\n"

print x
