hours=int(input())
if(hours<=2):
    print(30)
elif(hours>2 and hours<=23):
    print(30+(hours-2)*10)
elif(hours>=24):
    print(200)