ver = 0
gas = 0
alc = 0
die = 0
while ver!=4:
    ver = int(input())
    if ver == 1:
        alc+=1
    elif ver == 2:
        gas+=1
    elif ver == 3:
        die+=1
    elif ver == 4:
        break

print('MUITO OBRIGADO')   
print('Alcool:',alc)
print('Gasolina:',gas)
print('Diesel:',die)