x = []

for i in range(100):
    x.append(float(input()))

for i,obj in enumerate(x):
    if(obj<=10):
        print("A[%d] = %.1f"%(i,obj))
