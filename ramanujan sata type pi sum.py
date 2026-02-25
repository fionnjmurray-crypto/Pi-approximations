from decimal import Decimal, getcontext
getcontext().prec = 100000
import math
def abso(x):
    return (x**2)**0.5
def d(n):
    return Decimal(n)
def fact(n):
    n = int(n)
    result = d(1)
    for i in range(2, n + 1):
        result *= d(i)
    return result
def comb(n, r):
    n = int(n)
    r = int(r)
    return fact(n) / (fact(r) * fact(n - r))
def ntheuler(n):
    n = int(n)
    largesum = d(0)
    frontco = d(2 * n + 1)
    for l in range(2 * n + 1):
        flipper = d(-1) ** d(l)
        fractco = d(1) / ((d(2) ** d(l)) * (d(l) + d(1)))
        firscomb = comb(2 * n, l)
        smallsum = d(0)
        for q in range(l + 1):
            seccomb = comb(l, q)
            expo = (d(2 * q - 1)) ** d(2 * n)
            smallsum += seccomb * expo
        largesum += flipper * fractco * firscomb * smallsum
    return round((frontco * largesum * -1) + 2)

x=2
twoxtheuler = ntheuler(x)
largesum = d(0)
n=1
nthflipper = d(-1)**n
twopow = d(2**(x+2))
twoxfact = d(fact(2*x))
numerator = d(nthflipper * twopow * twoxfact)
xthflipper = d(-1)**x
polyn = d(2*n + 1)**d(2*x + 1)
denominator = d(xthflipper * polyn * twoxtheuler)
largesum += numerator / denominator


finalpi = d(abso(largesum))**d(1/(2*x + 1))

    
    
print(finalpi)

