a=int(input())
for i in range(1,a+1):
    if(i==1 or i==a):
        for j in range(1,a+1):
            print("*",end="")
        print()
    else:
        for  j in range(1,a+1):
            if(j==1 or j==a):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# 5
# *****
# *   *
# *   *
# *   *
# *****