x = []

for i in range(20):
    x.append(int(input()))

x.reverse()

for i,obj in enumerate(x):
    print("N[%d] = %d"%(i,obj))