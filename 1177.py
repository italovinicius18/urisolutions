n = int(input())
n
x = []

cont = 0
for i in range(1000):
    if cont==n:
        cont = n-cont
    x.append(cont)
    cont+=1

for i,obj in enumerate(x):
    print("N[%d] = %d"%(i,obj))