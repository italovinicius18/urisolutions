n = int(input())

for i in range(n):
    x = int(input())
    soma = 0
    for i in range(1,x):
        if x%i==0:
            soma+=i
    if soma == x:
        print("%d eh perfeito"%x)
    else:
        print("%d nao eh perfeito"%x)