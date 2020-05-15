total = 0
cont = 0
while True:
    try:
        s = input()
        dis = int(input())
        total += dis
        cont+=1
    except EOFError:
        print("%.1f" %(total/cont))
        break