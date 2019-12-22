#Copiei o código abaixo da internet
#https://github.com/MayaraMachado/URI---Python-3/blob/master/1118-Varias%20notas%20com%20valida%C3%A7ao.py 

con='n'
while True:
    cont,media,a=0,0,3
    while cont<2:
        X=float(input())
        if 0<=X<=10:
            cont+=1
            media+=X
        else:
            print("nota invalida")
    print('media = %.2f' %(media/2))
    while (a!=1 and a!=2):
        print("novo calculo (1-sim 2-nao)")
        a=int(input())
        if a==1:
            con='n'
        elif a==2:
            con='s'
        else:
            print("novo calculo (1-sim 2-nao)")
            a=int(input())


# Fiz esse algoritmo abaixo, está passando em todos os casos do Udebug, mas não sei pq dá runtime error

# cont = 0
# soma = 0
# ver = 0
# x = -1
# while True:
#     if cont==2:
#         print(f'media = %.2f'%(soma/2))
#         while True:
#             print('novo calculo (1-sim 2-nao)')
#             ver = int(input())
#             if ver==1:
#                 break
#             if ver==2:
#                 exit(0)
#         cont = 0
#         soma = 0
#     x = float(input())
#     if x>=0 and  x<=10:
#         cont+=1
#         soma+=x
#     else:
#         print('nota invalida')