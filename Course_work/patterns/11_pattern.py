# a=int(input()) #My own logic 
# for i in range(1,a+1):
#     if(i%2==0):
#         for j in range(1,i+1):
#             print(int(not(bool(j%2))),end=" ")
#         print()
#     else:
#         for j in range(1,i+1):
#             print((j%2),end=" ")
#         print()
# 5
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1 
 #Strivers logic
a=int(input())
start=1
for i in range(a):
    if(i%2==0):
        start=1
    else:
        start=0 
    for j in range(i+1):
        print(start,end="")
        start=1-start 
    print()


