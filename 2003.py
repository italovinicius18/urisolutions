while(True):
    try:
        t = list(map(int,input().split(":")))
        t = t[0]*60+t[1]
        if(t+60<=480):
            print("Atraso maximo: 0")
        else:
            print("Atraso maximo: %d"% (t+60-480))
    except EOFError:
        break