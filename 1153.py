def fact(n):
    soma = 1
    for i in range(n,0,-1):
        soma*=i
    print(soma)

n = int(input())
fact(n)