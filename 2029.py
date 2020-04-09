pi = 3.14
while(True):
    try:
        v = float(input())
        d = float(input())
        # v = pi*r²*h
        # a da boca = pi*r²
        h = v/(pi*(d/2)**2)
        a = pi*(d/2)**2
        print("ALTURA = %.2f"%h)
        print("AREA = %.2f"%a)
    except EOFError:
        break
