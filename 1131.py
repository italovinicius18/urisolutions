ver = 1
ocor = 0
vitI = 0
vitG = 0
emp = 0
while ver!=2:
    i,g = map(int,input().split())
    ocor+=1
    if i > g:
        vitI+=1
    elif g > i:
        vitG+=1
    else:
        emp+=1
    print('Novo grenal (1-sim 2-nao)')
    ver = int(input())

print(ocor,"grenais")
print('Inter:%d'%vitI)
print('Gremio:%d'%vitG)
print('Empates:%d'%emp)
if vitI > vitG:
    print('Inter venceu mais')
elif vitG > vitI:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')

