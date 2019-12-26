n = int(input())

for i in range(n):
    cont = 0
    x = input().split()
    pa,pb,ca,cb = int(x[0]),int(x[1]),float(x[2]),float(x[3])
    while(pb>=pa):
        pb = pb+int(pb*(cb/100))
        pa = pa+int(pa*(ca/100))
        cont+=1
        if cont>100:
            break
    if cont > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%cont)