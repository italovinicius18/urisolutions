n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    soma = 0
    if x%2==0:
        for j in range(y):
            soma+=x+1
            x+=2

    else:
        for j in range(y):
            soma+=x
            x+=2
    print(soma)