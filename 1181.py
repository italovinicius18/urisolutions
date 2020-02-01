l = int(input())
op = input()

soma = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if i == l:
            soma+=x

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/12))