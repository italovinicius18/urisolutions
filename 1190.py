op = input()

soma = 0
cont = 0
lim = 11
chegou = False

for i in range(12):
    for j in range(12):
        x = float(input())
        if i>0 and i<11 and j>lim:
            soma+=x
            cont+=1
    if(chegou):
        lim+=1
    elif(lim==6):
        chegou = True
    else:
        lim-=1
      
    

if op == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/cont))