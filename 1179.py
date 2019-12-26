x = []
for i in range(15):
    x.append(int(input()))
i = 0
j = 0
par = []
impar = []
for obj in x:
    if i == 5:
        i=0
        for a in par:
            print(a)
        par.clear()
    if j == 5:
        j = 0
        for a in impar:
            print(a)
        impar.clear()
    if obj%2==0:
        par.append("par[%d] = %d"%(i,obj))
        i+=1
    else:
        impar.append("impar[%d] = %d"%(j,obj))
        j+=1

for a in impar:
    print(a)
for a in par:
    print(a)