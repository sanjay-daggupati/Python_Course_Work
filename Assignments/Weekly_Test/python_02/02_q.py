n=int(input())
total_value=0
for _ in range(n):
    age=int(input())
    if(age>=5 and age<=18):
        total_value+=100 
    elif(age>18 and age<=60):
        total_value+=150
    elif(age>60):
        total_value+=150 
print(total_value)