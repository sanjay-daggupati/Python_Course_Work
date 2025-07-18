a=int(input())
for i in range(0,a):
    for j in range(0,a):
        if(j==i or j ==a-i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()