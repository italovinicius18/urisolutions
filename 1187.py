op = input()

soma = 0
cont = 0
l = 0
r = 11
for i in range(12):
    for j in range(12):
        x = float(input())
        if i < 5 and j>l and j<r:
            soma+=x
            cont+=1
    l+=1
    r-=1

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/cont))