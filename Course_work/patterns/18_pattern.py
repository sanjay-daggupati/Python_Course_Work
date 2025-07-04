a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(65+a-j),end=" ")
    print()
# 5
# E
# E D
# E D C
# E D C B
# E D C B A