n = int(input())

x = list(map(int,input().split()))

# Pode ser feito a partir das funções:
# min(x)
# import numpy as np
# index_min = np.argmin(x)

menor = 1000000000000
for i,obj in enumerate(x):
    if obj<menor:
        menor = obj
        pos = i

print("Menor valor: %d"%menor)
print("Posicao: %d"%pos)