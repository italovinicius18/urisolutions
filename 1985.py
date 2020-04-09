d = {1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}
total = 0
n = int(input())
for i in range(n):
    id, quant = map(float,input().split())
    total += d[id]*quant

print("%.2f" %total)
