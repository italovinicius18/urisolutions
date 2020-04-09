p, j1, j2, r, a = map(int, input().split())
total = j1+j2

# p = 1 -> j1 é par
# p = 0 -> j1 é impar

# r = 1 -> j1 roubou
# r = 0 -> j1 n roubou

# a = 1 -> j2 acusou
# a = 0 -> j2 n acusou

if(a==0 and r==0):
    if(p):
        if(total%2==0):
            j1vence = True
        else:
            j1vence = False
    else:
        if(total%2==0):
            j1vence = False
        else:
            j1vence = True
else:
    if(r):
        if(a):
            j1vence = False
        else:
            j1vence = True
    else:
        if(a):
            j1vence = True
        else:
            j1vence = False

if(j1vence):
    print("Jogador 1 ganha!")
else:
    print("Jogador 2 ganha!")

