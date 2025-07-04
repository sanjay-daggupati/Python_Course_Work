a=int(input())
for i in range(1,a+1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()
# 5
# A
# AB
# ABC
# ABCD
# ABCDE
