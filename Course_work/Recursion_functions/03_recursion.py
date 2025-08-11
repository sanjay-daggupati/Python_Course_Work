def decrease_number(n):
    if n==0:
        return 
    print(n,end=" ")
    decrease_number(n-1)


a=int(input())
decrease_number(a)