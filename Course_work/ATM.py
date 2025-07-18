user_data={
    1234567890:[1234,5000,[]],
    9876543210:[4321,6000,[]],
    1357913579:[2468,7000,[]],
    2468246810:[1357,8000,[]]
}
print("Welcome to the ATM")
Account_Number=int(input("Please Enter your account number:"))
pin=int(input("Enter your pin:"))
if(Account_Number in user_data and user_data[Account_Number][0]==pin):
    print("Login Successful")
    while(True):
        print("ATM MENU")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.WithDraw")
        print("4.View Transactions")
        print("5.Exit")
        ch=input("Enter your choice (1-5): ")
        if(ch=="1"):
            print(f"Balance :{user_data[Account_Number][1]}")
        elif(ch=="2"): 
            deposit=int(input("Enter your deposit ammount:"))
            user_data[Account_Number][1]=user_data[Account_Number][1]+deposit
            print(f"Amount sucessfully deposited {deposit}")
            user_data[Account_Number][2].append("Deposited "+str(deposit))
        elif(ch=="3"):
            withdrawl=int(input("Enter the amount you want to with drawl"))
            if(user_data[Account_Number][1]>withdrawl):
                user_data[Account_Number][1]=user_data[Account_Number][1]-withdrawl
                user_data[Account_Number][2].append("Withdrawl: "+str(withdrawl))
                print(f"Amount was sucessfully Withdrawn{withdrawl}")
            else:
                print(f"Balance is less than {withdrawl}")
        elif(ch=="4"):
            print("View History")
            for i in user_data[Account_Number][2]:
                print(i)
        elif(ch=="5"):
            print("Thanks for using atm")
            break
else:
    print("Wrong Account_number or pin entered")




