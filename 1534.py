while(1):
    try:
        x = int(input())
        if(x==0):
            break
        for i in range(x):
            for j in range(x):
                if(i+j==x-1):
                    print("2",end="")
                elif(i==j):
                    print("1",end="")
                else:
                    print("3",end="")
            print()
    except EOFError:
        break
