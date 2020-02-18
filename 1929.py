a,b,c,d = map(int,input().split())

if abs(b-c) < a and a < b+c and abs(a-c) < b and b < a+c  and abs(a-b) < c and c < a+b:
    print('S')
    exit()
if abs(b-d) < a and a < b+d and abs(a-d) < b and b < a+d  and abs(a-b) < d and d < a+b:
    print('S')
    exit()
if abs(d-c) < a and a < d+c and abs(a-c) < d and d < a+c  and abs(a-d) < c and c < a+d:
    print('S')
    exit()
if abs(b-c) < d and d < b+c and abs(d-c) < b and b < d+c  and abs(d-b) < c and c < d+b:
    print('S')
    exit()
else:
    print('N')