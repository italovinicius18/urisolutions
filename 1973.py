def main():
    from sys import stdin
    # Para os próximos usuários que tenham o mesmo problema em Python, a forma de solucionar é utilizando formas mais rápidas pra leitura e manipulação dos dados, no caso o stdin.readline()

    n = int(stdin.readline())

    x = list(map(int, stdin.readline().split()))

    i = 0
    atacado = [False]*n
    feito = False
    while not feito:

        atacado[i] = True
        aux = x[i]

        if(x[i]):
            x[i]-=1

        if(aux%2==0):
            i-=1
        else:
            i+=1

        if(i<0 or i>=n):
            feito = True

    print(atacado.count(True),sum(x))

if __name__ == "__main__":
    main()