n,m = map(int,input().split())

for i in range(m):
    x = input()
    if(x=="clicou"):
        n-=1
    else:
        n+=1

print(n)