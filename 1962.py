n = int(input())

for i in range(n):
    x = int(input())

    if(x>=2015):
        print(str(x-2015+1)+ " A.C.")
    else:
        print(str(2015-x)+ " D.C.")