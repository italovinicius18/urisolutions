def contar_substr(string,substring,pos):
    cont = 0
    inicio = 0
  
    while inicio <= pos: 
  
        tem_na_pos = string.find(substring, inicio) 
  
        if tem_na_pos != -1: 
            inicio = tem_na_pos + 1 
            cont += 1
        else: 
            return cont 

i = 1
while(True):
    try:
        n = input()
        m = input()

        print("Caso #%d:" % i)
        pos = m.rfind(n)+1
        qtd = contar_substr(m,n,pos)
        
        if(qtd != 0):
            print("Qtd.Subsequencias: %d"%qtd)
            print("Pos: %d" %pos)
        else:
            print("Nao existe subsequencia")
        print()
        i+=1

    except EOFError:
        break