from math import *

a = lambda x: (tan(x) - x) / (x ** 3)

b = lambda x: (exp(x) + cos(x) - sin(x) - 2.0) / (x ** 3)

i = 1

while True:

    print "{:d}   {:19.16f}".format(i, a(10 ** -i))

    if raw_input("") == "end":

        break

    i = i + 1

i = 1

while True:

    print "{:d} {:19.16f}".format(i, b(10 ** -i))

    if raw_input("") == "end":

        break

    i = i + 1
