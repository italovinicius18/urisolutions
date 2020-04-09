s,t,f = map(int,input().split())

hora = s+t+f

if(hora>=24):
    print(hora-24)
elif(hora<0):
    print(24+hora)
else:
    print(hora)