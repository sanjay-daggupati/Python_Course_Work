a=int(input())
for i in range(1,2*a+1):
    if(i<=a):
        for  j in range(a-i):
            print(" ",end="")
        for j in range((2*i)-1):
            print("*",end="")
        for j in range(a-i):
            print(" ",end="")
        print()
    if(i>a):
        for j in range(i-a-1):
            print(" ",end="")
        for j in range(2*(2*a-i)+1):
            print("*",end="")
        for j in range(i-a-1):
            print(" ",end="")
        print()
# 5
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
