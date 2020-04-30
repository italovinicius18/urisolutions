n = int(input())

op1 = ((1+5**(0.5))/2)**n
op2 = ((1-5**(0.5))/2)**n
div = 5**(0.5)

fibo = (op1-op2)/div

print("%.1f"%fibo)