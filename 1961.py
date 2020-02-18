p,n = map(int,input().split())

x = list(map(int,input().split()))

for i in range(n-1):
    if abs(x[i+1]-x[i]) > p:
        print('GAME OVER')
        exit()
print('YOU WIN')
