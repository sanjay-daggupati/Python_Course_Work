a=int(input())
for i in range(a):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(a-i)):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    print()
# 5
# *********
#  *******
#   *****
#    ***
#     *