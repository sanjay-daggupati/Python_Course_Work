a=int(input())
for i in range(2*a-1):
    for j in range(2*a-1):
        top=i
        left=j
        right=2*a-2-j
        down=2*a-2-i
        print(a-min(min(top,down),min(left,right)),end="")
    print()
# 5
# 555555555
# 544444445
# 543333345
# 543222345
# 543212345
# 543222345
# 543333345
# 544444445
# 555555555