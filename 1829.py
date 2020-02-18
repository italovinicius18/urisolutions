vence = ['tesoura','papel','pedra','lagarto','Spock']

perde = [['papel','lagarto'],['pedra','Spock'],['lagarto','tesoura'],['Spock','papel'],['tesoura','pedra']]

n = int(input())

for i in range(n):
    a,b = input().split()

    if(a==b) :
        print("Caso #%d: De novo!" %(i+1))
    elif b in perde[vence.index(a)] :
        print("Caso #%d: Bazinga!" %(i+1))
    elif a in perde[vence.index(b)] :
        print("Caso #%d: Raj trapaceou!" %(i+1))