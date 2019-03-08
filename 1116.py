n=int(input())
for i in range(n):
  try:
    x,y=map(int,input().split())
    z=round((x/y),1)
    print(z)
  except ZeroDivisionError:
    print("divisao impossivel")