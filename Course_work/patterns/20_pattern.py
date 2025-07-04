a=int(input())
for i in range(1,2*a):
    if(i<=a):
        for j in range(1,i+1):
            print("*",end="")
        for j in range(1,2*(a-i)+1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end="")
        print()
    else:
        for j in range(1,(2*a-i)+1):
            print("*",end="")
        for j in range(1,2*(i-a)+1):
            print(" ",end="")
        for j in range(1,(2*a-i)+1):
            print("*",end="")
        print()
#5
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
        