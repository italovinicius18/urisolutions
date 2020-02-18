n = int(input())

for i in range(n):
    x = input().split()
    a,b = map(int,input().split())
    if((a+b)%2==0):
        if(x[1]=='PAR'):
            print(x[0])
        else:
            print(x[2])
    else:
        if(x[1]=='IMPAR'):
            print(x[0])
        else:
            print(x[2])