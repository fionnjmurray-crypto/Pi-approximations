from decimal import Decimal, getcontext
getcontext().prec = 1000
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
n=0
pin = d(0)
while True:
   numerator = d(((-1)**n) * 8257536)
   denominator = d(277) * d(((2*n + 1)**9))
   pasum = d(numerator/denominator)
   pin += d(pasum)
   pi = d(pin)**(d(1)/d(9))
   print(f"{pi} - {n}")
   n+=1
