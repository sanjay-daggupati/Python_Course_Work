def increase_number(a):
    if(a==0):
        return
    increase_number(a-1)
    print(a,end=" ")
a=int(input())
increase_number(a)
