n1 = float(input())
i=0
t=float(0)
if n1>0:
   i+=1
   t+=n1
n2 = float(input())
if n2>0:
   i+=1
   t += n2
n3 = float(input())
if n3>0:
   i+=1
   t += n3
n4 = float(input())
if n4>0:
   i+=1
   t += n4
n5 = float(input())
if n5>0:
   i+=1
   t += n5
n6 = float(input())
if n6>0:
   i+=1
   t += n6

p=round(t/i,1)

print(i,'valores positivos')
print(p)
