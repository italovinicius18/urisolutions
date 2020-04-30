n = int(input())

for i in range(n):
    h,m,o = map(int,input().split())
    print("%02d:%02d - "%(h,m),end="")
    if(o):
        print("A porta abriu!")
    else:
        print("A porta fechou!")