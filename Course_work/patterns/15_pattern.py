a=int(input())
for i in range(a):
    for j in range(65,65+(a-i)):
        print(chr(j),end="")
    print()
# 5
# ABCDE
# ABCD
# ABC
# AB
# A