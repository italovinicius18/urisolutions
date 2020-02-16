while(True):
    x = int(input())
    a = 1
    if(x==0):
        break
    for i in range(x):
        b = a
        for j in range(x):
            b*=2
            t = b
        a*=2
    t//=2
    t = len(str(t))
    a = 1
    for i in range(x):
        b = a
        for j in range(x):
            if(j==0):
                print(str(b).rjust(t),end="")
            else:
                print(str(b).rjust(t+1),end="")
            b*=2
        a*=2
        print()
    print()