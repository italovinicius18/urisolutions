x = list(map(int,input().split()))
x.sort()

z = x[-2]
x = x[-1]
cont = 0
soma = 0

while soma<x:
    soma+=z
    z+=1
    cont+=1

print(cont)