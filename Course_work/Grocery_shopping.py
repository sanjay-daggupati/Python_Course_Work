Products={
    1:["Rice",60.],
    2:["Wheat Flour",100],
    3:["Cooking Oil",120],
    4:["Tea Powder",90],
    5:["Bread",30],
    6:["Soap",25],
    7:["Salt",20],
    8:["Egg(12pcs)",70],
    9:["Milk",25],
    10:["Sugar",40]   
}
print("Welcome to BHAAI Market".center(30,"-"))
print("Products Available")
print("Index".ljust(10," "),"Product".ljust(10," "),"Price".rjust(10," "))
Quantities,Prices=[],[]
for i,v in Products.items():
    print(f"{str(i).ljust(10," ")}{v[0].ljust(10," ")}{(str(v[1]).rjust(10," "))}")
print("Enter the products that you want to buy in index")
print("Enter the index")
Cart=list(map(int,input().split()))
print("".join(str(Cart)))
index=set()
total=0
print(f"{"Index".ljust(10," ")}{"Product".ljust(20," ")}{"Price".ljust(15," ")}{"Quantity".center(10," ")}")
for i in Cart:
    if i not in index:
        index.add(i)
        print(f"{str(i).ljust(10," ")}{Products[i][0].ljust(10," ")}{(str(Products[i][1]).ljust(15," "))}{(str(Cart.count(i)).center(10," "))}")
        total+=((Products[i][1])*Cart.count(i))
print(f'{"TotalBill".ljust(30," ")} {total}')


