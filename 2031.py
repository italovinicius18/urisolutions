def resultado(m1,m2):
    if(m1=="ataque" and m2=="pedra"):
        print("Jogador 1 venceu")
    elif(m2=="ataque" and m1=="pedra"):
        print("Jogador 2 venceu")
    elif(m1=="pedra" and m2=="papel"):
        print("Jogador 1 venceu")
    elif(m2=="pedra" and m1=="papel"):
        print("Jogador 2 venceu")
    elif(m1=="papel" and m2=="ataque"):
        print("Jogador 2 venceu")
    elif(m2=="papel" and m1=="ataque"):
        print("Jogador 1 venceu")
    elif(m1=="papel" and m2=="papel"):
        print("Ambos venceram")
    elif(m1=="pedra" and m2=="pedra" or m2=="pedra" and m1=="pedra"):
        print("Sem ganhador")  
    elif(m1=="ataque" and m2=="ataque" or m1=="ataque" and m2=="ataque"):
        print("Aniquilacao mutua") 




n = int(input())
for i in range(n):
    m1 = input()
    m2 = input()
    resultado(m1.lower(),m2.lower())