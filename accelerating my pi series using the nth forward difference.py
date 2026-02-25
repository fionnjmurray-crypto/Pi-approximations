from decimal import Decimal, getcontext
getcontext().prec = 100000
def d(n):
    return Decimal(n)
def facto(num):
    result  = num
    while num > 2:
        result *= num - 1
        num -= 1
    if num == 0:
        return 1
    return result

def pi(k):
    n=0
    pin = d(0)
    while n <= k:
       numerator = d(((-1)**n) * 2**14 * facto(12))
       denominator = d(2702765) * d(((2*n + 1)**13))
       pasum = d(numerator/denominator)
       pin += d(pasum)
       n+=1
    return d(pin)**(d(1)/d(13))
loop= int(input("input iterations"))
print(pi(loop))
