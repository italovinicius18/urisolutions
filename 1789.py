while(1):
    try:
        l = int(input())
        v = list(map(int,input().split()))

        rapida = max(v)

        if(rapida<10):
            print(1)
        elif(rapida >= 10 and rapida <20):
            print(2)
        else:
            print(3)
    except EOFError:
        break