a=int(input())
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(j,end="")
    print()
# 5
# 1234
# 123
# 12
# 1