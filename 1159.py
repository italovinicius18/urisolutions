while True:
    x= int(input())
    if x ==0:
        break
    soma = 0
    if x%2==0:
        for j in range(5):
            soma+=x
            x+=2
    else:
        for j in range(5):
            soma+=x+1
            x+=2
    print(soma)