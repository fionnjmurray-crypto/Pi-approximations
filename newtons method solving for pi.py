import math
from decimal import Decimal, getcontext
getcontext().prec = 100
def d(n):
    return Decimal(n)
def newt(g):
    newt = d(g)
    for i in range(100):
        newt = d(g) - d(math.tan(d(g)))
        g = d(newt)
    return newt
print(newt(d(3)))
