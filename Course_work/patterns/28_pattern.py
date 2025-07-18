a=int(input())
for i in range(a):
    for j in range(a):
        if((i==0  and j!=0 and j!=a-1) or (j==0 and i<a//2) or (j==a-1 and i>a//2) or (i==a//2 and j!=0 and j!=a-1) or(i==a-1 and j!=a-1 and j!=0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()