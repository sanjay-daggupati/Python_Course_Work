a=int(input())
for i in range(1,2*a+1):
    if(i<=a):
        for j in range(a-i+1):
            print("*",end="")
        for j in range(2*(i-1)):
            print(" ",end="")
        for j in range(a-i+1):
            print("*",end="")
        print()
    else:
        for j in range(i-a):
            print("*",end="")
        for j in range(2*a-2*(i-a)):
            print(" ",end="")
        for j in range(i-a):
            print("*",end="")
        print()


# 5
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********