cont = 0
soma = 0
while True:
    if (cont==2):
        print("media =",round(soma/2,2))
        break
    x = float(input())
    if x>=0 and  x<=10:
        cont+=1
        soma+=x
    else:
        print('nota invalida')
