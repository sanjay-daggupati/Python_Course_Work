# a=int(input())
# for i in range(1,a+1):
#     for j in range(a-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(chr(65+j-1),end="")
#     for j in range(i-1,0,-1):
#         print(chr(65+j-1),end="")
#     for j in range(a-i):
#         print(" ",end="")
#     print()
# 5
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
# Strivers logic 
a=int(input())
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    char=64
    Symmetry=((2*i-1)//2)+1
    for j in range(2*i-1):
        if(j<Symmetry):
            char+=1
            print(chr(char),end="")
        else: 
            char-=1
            print(chr(char),end="")
    for j in range(a-i):
        print(" ",end="")
    print()
# 5
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA