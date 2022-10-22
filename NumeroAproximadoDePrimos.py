from math import log

n = float(input())
P = n / log(n)
M = 1.25506 * (n / log(n))
print("%.1f %.1f" % (P, M))
