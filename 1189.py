op = input()

soma = 0
cont = 0
u = 0
d = 11
lim = 0
ver = True
for i in range(12):
    for j in range(12):
        x = float(input())
        if i > u and i<d and j<lim:
            soma+=x
            cont+=1
    if ver:
        lim+=1
    elif not ver:
        lim-=1
    if lim == 6:
        lim-=1
        ver = False
    

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/cont))