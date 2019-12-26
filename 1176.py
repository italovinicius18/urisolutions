def fibo(n):
    seq = [0,1]
    for i in range(2,n):
        seq.append(seq[i-1]+seq[i-2])
    return seq

fib = fibo(61)

n = int(input())

for i in range(n):
    x = int(input())
    print("Fib(%d) = %d"%(x,fib[x]))