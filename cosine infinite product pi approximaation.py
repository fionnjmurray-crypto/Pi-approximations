psqoe = 0
n = 1
while True:
    
    psqoe += (2*n - 1)**-2
    psq = psqoe*8
    p = psq**0.5
    print(f"{p} - {n}")
    n+= 1    
