def sum_of_numbers(a):
    if(a==1):
        return 1
    else:
        return a+sum_of_numbers(a-1)

a=int(input())

print(sum_of_numbers(a))