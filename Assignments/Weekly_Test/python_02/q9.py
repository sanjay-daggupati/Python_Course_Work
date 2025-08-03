pin =1234
for _ in range(3):
    epin=input()
    if(epin==pin):
        print("Access Granted")
        break
else:
    print("ATM Blocked.Try again Later")