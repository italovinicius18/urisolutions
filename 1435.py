#Solução abixo está com TLE

import math
while(True):
    x = int(input())
    if(x==0):
        break
    for i in range(x):
        for j in range(x):
            for k in range(math.ceil(x/2)):
                if(i == k or i == x-(k+1) or j == k or j == x-(k+1)):
                    if(len(str(k+1))==2 or j==0):
                        print("  "+str(k+1),end="")
                        break
                    else:
                        print("   "+str(k+1),end="")
                        break
        print()
    print()

#Este código é de um reõsitório que encontrei
# https://github.com/mrmourao/uri-online-judge-in-python/blob/master/uri_1435_Matriz_Quadrada_I.py

while True:
    N = int(input())

    if (N == 0):
        break

    resultado =  []

    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(1)
        resultado.append(tmp)

    valor = 1
    cima = 0
    esq = 0
    baixo = N - 1
    direita = N - 1

    if (N % 2 == 0):
        meio = N / 2

    else:
        meio = (N + 1) / 2


    while (valor <= meio):
        i = esq
        while (i <= direita):
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i+=1

        i = (cima + 1)
        while ( i < baixo):
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i+=1

        valor+=1
        cima+=1
        baixo-=1
        esq+=1
        direita-=1

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %resultado[i][j]
        print(tx[1:])
    print("")