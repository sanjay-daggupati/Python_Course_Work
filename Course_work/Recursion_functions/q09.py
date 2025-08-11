def countdown(n):
    while(n>=0):
        yield(n)
        n=n-1  
n=int(input())
numbers=countdown(n)
for number in numbers:
    print(number)

