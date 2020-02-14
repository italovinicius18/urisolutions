while(True):
    try:
        a,b,c = map(int,input().split())
        d = a*b
        e = (d*100)//c
        print("%d"%(e**(0.5)))
    except ValueError:
        break
