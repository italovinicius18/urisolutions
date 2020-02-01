op = input()

soma = 0
cont = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if j > i:
            soma+=x
            cont+=1

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/cont))