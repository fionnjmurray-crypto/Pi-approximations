base = 1
count = 1
flipper = -1
while True:
    count += 2
    recip = 1/count
    recip *= flipper
    base += recip
    esti = base * 4
    print(esti)
    flipper *= -1
    
