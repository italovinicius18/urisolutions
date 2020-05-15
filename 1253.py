n = int(input())

for j in range(n):

    s = input()
    q = int(input())
    x = []
    for i in s:
        if (ord(i)-q >= 65 and ord(i)-q <= 90) or (ord(i)-q >= 97 and ord(i)-q <= 122):
            x.append(chr(ord(i)-q))
        else:
            x.append(chr(ord(i)+(26-q)))
    print(''.join(x))
