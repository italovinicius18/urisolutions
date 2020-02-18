n = int(input())

x = [int(i) for i in input().split()]

i = 0
atacado = [False]*n
while(i>=0 and i < n):
    aux = x[i]
    if(x[i]>0):
        x[i]-=1
        atacado[i] = True
    if(aux%2==0):
        i-=1
    else:
        i+=1

print(atacado.count(True),sum(x))