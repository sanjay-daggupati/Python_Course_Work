a=int(input())
for i in range(1,2*a):
    if(i<=a):
        for j in range(i):
            print("*",end="")
        print()
    else:
        for j in range(2*a-i):
            print("*",end="")
        print()
# 5
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *     