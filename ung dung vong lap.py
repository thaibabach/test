import math         #bai tap: phan tich mot so thanh thua so nguyen to
so_ngto = [0] * 100
def so_nguyen_to ():        #ham tim so nguyen to trong khoang 1 den 100
    a = [True] * 100
    a[0] = False
    a[1] = False
    for i in range (2, int(math.sqrt(100)) + 1):        #hai vong for tim so nguyen to trong khoang 1 den 100
        if a[i] == True:
            for j in range (i*i, 100, i):
                a[j] = False
    j = 0
    for i in range (100):
        if a[i] == True:
            so_ngto[j] = i
            j += 1

def phan_tich (n):
    a = [0] * 100
    j=0;
    for i in so_ngto:
        if (i == 0): break
        while (n%i == 0 and n!=1):
            n/=i
            a[j] += 1
        j+=1
    for i in range (j):
        if (a[i] != 0):
            print ((str(so_ngto[i]) + " ") * a[i], end = " ")
so_nguyen_to()
phan_tich(54)
