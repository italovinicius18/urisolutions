n = int(input())

xs = list(map(int,input().split()))

pico,vale = False,False

if n==1:
    print(1)
    exit()
if n==2 and xs[0]!=xs[1]:
    print(1)
    exit()

if xs[1]>xs[0] and xs[1]>xs[2]:
    pico = True
if xs[1]<xs[0] and xs[1]<xs[2]:
    vale = True

for i in range(3,n-1,2):
    if (pico):
        if not(xs[i]>xs[i-1] and xs[i]>xs[i+1]):
            print(0)
            exit()
    if (vale):
        if not(xs[i]<xs[i-1] and xs[i]<xs[i+1]):
            print(0)
            exit()

if pico or vale:
    print(1)
else:
    print(0)