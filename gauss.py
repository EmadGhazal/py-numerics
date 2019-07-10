import numpy as np

from io import StringIO

import sys

def gauss(A, b):

    n = A.shape[0]

    for j in xrange(n - 1):

        #if abs(A[j][j]) == 0:

            #print "Error: zero pivot encountered."

            #sys.exit()

        for i in xrange(j + 1, n):

            mult = A[i][j] / A[j][j]

            for k in xrange(j + 1, n):

                A[i][k] = A[i][k] - mult * A[j][k]

            b[i] = b[i] - mult * b[j]

    x = np.copy(b)

    for i in xrange(n - 1, -1, -1):

        for j in xrange(i + 1, n):

            x[i] = x[i] - A[i][j] * x[j]

        x[i] = x[i] / A[i][i]

    return x

"""A_in = 
        4 -2 2

        -2 1 3

        2 -2 2
            

b_in = 
        1

        1

        1
        

A = np.genfromtxt(StringIO(unicode(A_in)), delimiter = " ")

b = np.genfromtxt(StringIO(unicode(b_in)), delimiter = " ")

x = gauss(A, b)

print A

print b

print x
"""
