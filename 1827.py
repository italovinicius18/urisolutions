while(1):
    try:
        x = int(input())
        for i in range(x):
            for j in range(x):
                if((x+1)/2==i+1 and (x+1)/2==j+1):
                    print(4,end="")
                elif(i>=(x//3) and i<(x-(x/3)) and j>=(x//3) and j<(x-(x//3))):
                    print(1,end="")
                elif(i+j==x-1):
                    print(3,end="")
                elif(i==j):
                    print(2,end="")
                else:
                    print(0,end="")
            print()
        print()
    except EOFError:
        break