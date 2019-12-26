def fibo(n):
    seq = [0,1]
    for i in range(2,n):
        seq.append(seq[i-1]+seq[i-2])
    print (' '.join(str(x) for x in seq))

n = int(input())
fibo(n)