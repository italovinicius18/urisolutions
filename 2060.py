n = int(input())
xs = list(map(int,input().split()))
div2,div3,div4,div5 = 0,0,0,0
for i in xs:
    if i%2==0:
        div2+=1
    if i%3==0:
        div3+=1
    if i%4==0:
        div4+=1
    if i%5==0:
        div5+=1

print("%d Multiplo(s) de 2"%div2)
print("%d Multiplo(s) de 3"%div3)
print("%d Multiplo(s) de 4"%div4)
print("%d Multiplo(s) de 5"%div5)