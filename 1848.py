for i in range(3):
    soma = 0
    while(1):
        x = input()
        if(x=='caw caw'):
            break
        if(x[0]=='-'):
            if(x[1]=='-'):
                if(x[2]=='-'):
                    soma+=0
                else:
                    soma+=1
            else:
                if(x[2]=='-'):
                    soma+=2
                else:
                    soma+=3
        elif(x[0]=='*'):
            if(x[1]=='-'):
                if(x[2]=='-'):
                    soma+=4
                else:
                    soma+=5
            else:
                if(x[2]=='-'):
                    soma+=6
                else:
                    soma+=7
    print(soma)
    