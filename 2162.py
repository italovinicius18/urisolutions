def picos_vales(n,xs):
    for i in range(n-1):
        if xs[i] < xs[i+1]:
            if (i!=0 and relevo == 1):
                return 0
            relevo = 1
        elif xs[i] > xs[i+1]:
            if (i!=0 and relevo == 0):
                return 0
            relevo = 0
        else:
            return 0
    return 1
    
n = int(input())

xs = list(map(int,input().split()))

print(picos_vales(n,xs))