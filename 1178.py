n = float(input())

x = [n]

for i in range(1,100):
    x.append(x[i-1]/2)

for i,obj in enumerate(x):
    print("N[%d] = %.4f"%(i,obj))