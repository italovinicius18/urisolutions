while(True):
    x = int(input())
    if(x==0):
        break
    for i in range(x):
        id = False
        a = i+1
        for j in range(x):
            if(j==0):
                print("%3d"%a,end="")
            else:
                print("%4d"%a,end="")
            if(i==j):
                id = True
            if(id):
                a+=1
            else:
                a-=1
        print()
    print()