dic = {1: 0,
       2: 31,
       3: 60,
       4: 91,
       5: 121,
       6: 152,
       7: 182,
       8: 213,
       9: 244,
       10: 274,
       11: 305,
       12: 335}

dia_natal = dic[12]+25

while(True):
    try:
        m, d = map(int, input().split())
        dia_atual = dic[m]+d
        if(dia_atual == dia_natal):
            print("E natal!")
        elif(dia_atual == dia_natal-1):
            print("E vespera de natal!")
        elif(dia_atual > dia_natal):
            print("Ja passou!")
        else:
            print("Faltam %d dias para o natal!" % (dia_natal-dia_atual))
    except EOFError:
        break