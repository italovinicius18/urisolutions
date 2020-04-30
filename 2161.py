def decimos(fracao, n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1/6
    else:
        return 1/(6+decimos(fracao, n-1))


n = int(input())

decimos = decimos(1/6, n)


print("%.10f" % (3+decimos))