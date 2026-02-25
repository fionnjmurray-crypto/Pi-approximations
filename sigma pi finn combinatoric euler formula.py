import math
def facto(num):
    result  = num
    while num > 2:
        result *= num - 1
        num -= 1
    if num == 0:
        return 1
    return result

def comb(n, k):
    nume = facto(n)
    denom = facto(k) * (facto(n-k))
    return(nume/denom)

def eule(n):
    if n % 2 == 1:
        return 0
    bigsum = 0
    for k in range(n+1):
        vart = ((-1)**k) / (2**k)
        smallsum = 0
        for m in range(2*k + 1):
            raav = math.comb(2*k, m) * ((k-m)**(n))
            smallsum += raav
        bigsum += vart * smallsum
    return int(bigsum/(math.factorial(n)))

for i in range(10):
    print(f"E{i} = {eule(i)}")
