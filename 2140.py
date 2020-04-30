notas = [100,50,20,10,5,2]

while(True):
    n, m = map(int, input().split())
    possivel = False
    if(n == 0 and m == 0):
        break
    cont = 0
    troco = m-n

    for i in notas:
        for j in notas:
            if(i+j==troco):
                possivel = True
                break

    
    if(possivel):
        print("possible")
    else:
        print("impossible")