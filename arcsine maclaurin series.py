import math
def facto(num):
    result  = num
    while num > 2:
        result *= num - 1
        num -= 1
    if num == 0:
        return 1
    return result
n=0
hapi= 0
counter = 0
while hapi*2 !=  math.asin(1)*2:
    nom = facto(2*n)
    four = 4**n
    nfsq = facto(n)**2
    bii = 2*n + 1
    denom = four * nfsq * bii
    yea =  nom/denom
    hapi += yea
    n+=1
    print(f"{hapi*2} - {counter}")
    counter += 1
