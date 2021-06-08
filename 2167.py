n = int(input())
xs = list(map(int,input().split()))

for i in range(1,n):
    if(xs[i]<xs[i-1]):
        print(i+1)
        exit()
print(0)