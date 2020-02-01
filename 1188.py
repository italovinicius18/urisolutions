op = input()

soma = 0
cont = 0
l = 4
r = 7
for i in range(12):
    for j in range(12):
        x = float(input())
        if i > 6 and j>l and j<r:
            soma+=x
            cont+=1
    if i > 6:
        l-=1
        r+=1

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/cont))