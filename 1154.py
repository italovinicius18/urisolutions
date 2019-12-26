def average_years():
    n = 0
    cont = 0
    soma = 0
    while True:
        n = int(input())
        if(n<0):
            break
        soma+=n
        cont+=1
    print("%.2f"%(soma/cont))

average_years()