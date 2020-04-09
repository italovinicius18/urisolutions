caso=1
while(True):
    try:
        n = int(input())
        l = [0]
        max = 1
        for i in range(0,n+1):
            for j in range(0,i):
                l.append(i)
            max+=1
        if(len(l)==1):
            print("Caso %d: %d numero" %(caso,len(l)))
        else:
            print("Caso %d: %d numeros" %(caso,len(l)))
        print(" ".join(str(i) for i in l))
        print()
        caso+=1

    except EOFError:
        break