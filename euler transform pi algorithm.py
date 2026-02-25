import math
from decimal import Decimal as d, getcontext
getcontext().prec = 999999
def F(n):
    return math.factorial(n)
def C(n,k):
    n = int(n)
    k = int(k)
    return (F(n)) / (F(k)*F(n-k))

def a(n):
    numerator = (7847962214400) # 2^14 * 12!
    denominator = 2702765 * ((2*n + 1)**13)
    return d(numerator) / d(denominator)
def nthfdaz(n):
    summer = 0
    for k in range(n+1):
        flipper = (-1)**k
        comb = C(n, k)
        summer += d(flipper) * d(comb) * d(a(n-k))
    return summer
def S(i):
    summer = 0
    for n in range(i+1):
        flipper = (-1)**n
        summer += d(flipper)*d(a(n))
    return summer
def thrt(x):
    return d(x)**d((d(1)/d(13)))
def Se(i):
    summer = 0
    for n in range(i+1):
        flipper = (-1)**n
        fract = d(nthfdaz(n))/d(2**(n+1))
        summer += d(flipper) * d(fract)
    return summer
while True:
    lim = int(input("input accuracy for pi: ")) + 1
    for i in range(lim):
        guess = thrt(S(i))
        print(round(guess, i*10))

        
