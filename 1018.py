r=int(input())

r1=r%100
x1=int((r-r1)/100)
r2=r1%50
x2=int((r1-r2)/50)
r3=r2%20
x3=int((r2-r3)/20)
r4=r3%10
x4=int((r3-r4)/10)
r5=r4%5
x5=int((r4-r5)/5)
r6=r5%2
x6=int((r5-r6)/2)
r7=r6%1
x7=int((r6-r7)/1)

print(r)
print(x1,'nota(s) de R$ 100,00')
print(x2,'nota(s) de R$ 50,00')
print(x3,'nota(s) de R$ 20,00')
print(x4,'nota(s) de R$ 10,00')
print(x5,'nota(s) de R$ 5,00')
print(x6,'nota(s) de R$ 2,00')
print(x7,'nota(s) de R$ 1,00')