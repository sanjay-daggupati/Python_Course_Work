## Budget Details
Id=int(input("Enter user id: "))
Name =input("Enter your name: ")
Income=float(input("Enter yout income in decimal values :"))
Expense_Categories=list(input("More Expense Happens for: ").split())
Expense_amount=tuple(map(int,input("Amount for Each Expense: ").split()))
Everymonth_Bill=set(input("Bills that occur again: ").split())
Bank_details=eval(input("Please give your Bank details: "))
Saving_goal=float(input("How much percentage do you want to save: "))
user_info={
    "Name":Name,
    "ID":Id
}
print()
print("User_name, Id: ",end="")
print(Name,Id,sep=",")
print(f"Monthly_Income: {Income}")
print("Saving Goal :%.2f%%" %Saving_goal)
print("Bank:Details Bank -{Bank}, Account -{Account}, Branch -{Branch}".format(**Bank_details))
print("Name: {Name}, Id:{ID}".format_map(user_info))
# Enter user id: 007
# Enter your name: JamesBond
# Enter yout income in decimal values :500000.00
# More Expense Happens for: Ammunation Clothes Cars Accesories
# Amount for Each Expense: 200000 50000 100000 20000
# Bills that occur again: Electricity Netflix MilkBasketBill
# Please give your Bank details: {"Bank":"M16-Bank","Account":234584638,"Branch":"London"}
# How much percentage do you want to save: 30.00

# User_name, Id: JamesBond,7
# Monthly_Income: 500000.0
# Saving Goal :30.00%
# Bank:Details Bank -M16-Bank, Account -234584638, Branch -London
# Name: JamesBond, Id:7