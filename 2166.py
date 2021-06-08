def sqrt(n):
    if n==0:
        return 0
    else:
        n-=1
        return 1/(2+sqrt(n))

n = int(input())

print("%.10f" %(1+sqrt(n)))