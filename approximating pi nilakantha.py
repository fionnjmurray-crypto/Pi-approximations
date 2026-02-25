esti = 3
count = 2
flipper = 1
while True:
    recip = 4/(count*(count+1)*(count+2))
    recip *= flipper
    esti += recip
    print(esti)
    flipper *= -1
    count += 2
