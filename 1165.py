n = int(input())

for i in range(n):
    x = int(input())
    cont = 0
    for i in range(1,x+1):
        if x%i==0:
            cont+=1
        if cont > 2:
            break
    if cont > 2:
        print("%d nao eh primo"%x)
    else:
        print("%d eh primo"%x)