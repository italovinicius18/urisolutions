n = int(input())
maior = 0

for i in range(n):
    m,nota = map(float,input().split())
    if(nota>maior):
        maior = nota
        id = m

if(maior>=8):
    print(int(id))
else:
    print("Minimum note not reached")
