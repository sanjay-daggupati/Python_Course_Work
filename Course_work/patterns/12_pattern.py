a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(2*(a-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
# 4
# 1      1
# 12    21
# 123  321
# 12344321