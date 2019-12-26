x = int(input())
z = -100000000000

while z<=x:
    z = int(input())

cont = 0
soma = 0

while soma<=z:
    soma+=x
    x+=1
    cont+=1

print(cont)