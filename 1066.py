p = int(0)
i = int(0)
pos = int(0)
neg = int(0)
n1 = int(input())
if n1%2==0:
   p+=1
if n1%2!=0:
   i+=1
if n1>0:
   pos+=1
if n1<0:
   neg+=1

n2 = int(input())
if n2%2==0:
   p+=1
if n2%2!=0:
   i+=1
if n2>0:
   pos+=1
if n2<0:
   neg+=1

n3 = int(input())
if n3%2==0:
   p+=1
if n3%2!=0:
   i+=1
if n3>0:
   pos+=1
if n3<0:
   neg+=1

n4 = int(input())
if n4%2==0:
   p+=1
if n4%2!=0:
   i+=1
if n4>0:
   pos+=1
if n4<0:
   neg+=1

n5 = int(input())
if n5%2==0:
   p+=1
if n5%2!=0:
   i+=1
if n5>0:
   pos+=1
if n5<0:
   neg+=1


print(p,'valor(es) par(es)')
print(i,'valor(es) impar(es)')
print(pos,'valor(es) positivo(s)')
print(neg,'valor(es) negativo(s)')