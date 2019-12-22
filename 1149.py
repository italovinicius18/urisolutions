s = input().split()
l = []
soma = 0

l.append(int(s[0]))

for i in range(1,len(s)):
    i = int(s[i])
    if i>0:
        l.append(i)
        break

for i in range(l[1]):
    soma+=l[0]
    l[0]+=1

print(soma)