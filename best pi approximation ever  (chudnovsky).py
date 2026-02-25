def facto(num):
    result  = num
    while num > 2:
        result *= num - 1
        num -= 1
    if num == 0:
        return 1
    return result
invtwlvp = 0
for k in range(0,10):
    plmn = (-1)**k
    snf = facto(6*k)
    longco =  (545140134*k)+13591409
    tnf = facto(3*k)
    nfc = (facto(k))**3
    longba = 640320
    funkyexpo = (3*k) + 1.5
    invtwlvpTALLY = (plmn*snf*longco)/(tnf*nfc*(longba**funkyexpo))
    invtwlvp += invtwlvpTALLY


twlvp = invtwlvp**(-1)
pi = twlvp/12
print(pi)
