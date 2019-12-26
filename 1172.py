x = []
for i in range(10):
    x.append(int(input()))

for i,obj in enumerate(x):
    if obj<=0:
        print("X[%d] = 1"%i)
    else:
        print("X[%d] = %d"%(i,obj))