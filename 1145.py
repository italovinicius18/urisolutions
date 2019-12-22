x,y = map(int,input().split())
cont = 0
for i in range(1,y+1):
    if (cont==x):
        cont = 1
        print(i,end=" ")
    else:
        if cont != x-1 and i==y:
            print(i,end=" ")
            exit(0)
        if cont == x-1:
            print(i)
            cont+=1
        else:
            print(i,end=" ")
            cont+=1