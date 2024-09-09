from math import sqrt
sayı = int(input("enter a number: "))
bolen = 2
    
def find_root(num, bolen):
    bolebilenler = []
    out = []
    ins = []
    mult = 1
    mult2 = 1
    tam = False
    if int(sqrt(num)) == sqrt(num):
        print(int(sqrt(num)),end="")
        tam = True
    else:
        for i in range(num+1):
            if num % bolen==0:
                num = num/bolen
                bolebilenler.append(bolen)
            else:
                bolen += 1
    
    for a in bolebilenler:
        x = bolebilenler.count(a)
        if x == 1:
            ins.append(a)
        else:
            out.append(a)
    for b in out:
        while int(out.count(b))%2!=0:
            out.remove(b)
            ins.append(b)

    for o in out:
        mult = mult*o 
    for e in ins:
        mult2 = mult2*e

    sqr = sqrt(mult)
    if tam == False:
        if int(sqr)==1:
            print(f"answer: √{mult2}",end="")
            print(f"root({mult2})",end="")
        else:
            print(f"answer: {int(sqr)}√{mult2}",end="")


if sayı >= 0:
    find_root(sayı,bolen)
elif sayı < 0:
    sayı = sayı * (-1)
    find_root(sayı,bolen)
    print("i")





