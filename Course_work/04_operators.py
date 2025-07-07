# Arthimetic operators
print("Arthemetic Operators")
a=10
b=20
print(f"addition:{a+b}")
print(f"Subraction:{a-b}")
print(f"Multiplication :{a*b}")
print(f"Divison :{a/b}")
print(f"Floor Divison:{b//a}")
print(f"Remainder :{a%b}")
print(F"Exp(**):{a**b}")
# addition:30
# Subraction:-10
# Multiplication :200
# Divison :0.5
# Floor Divison:2
# Remainder :10
# Exp(**):100000000000000000000
print()
## Comparison operators
print("Comparison operators")
a=10
b=20
print("Eqa(==):",a==b)
print(f"Neqa(!=): {a!=b}")
print(f"Gre(>): {a>b}")
print(f"Les(<): {a<b}")
print(f"GreEqa(>=):{a>=b}")
print(f"LessEqa(<=):{a<=b}")
# Eqa(==): False
# Neqa(!=): True
# Gre(>): False
# Les(<): True
# GreEqa(>=):False
# LessEqa(<=):True
print()
##Assignment operators
print("Assignment operators")
b=20
b+=30
print("Add and assign(+=):",b)
b-=10
print("Subract and assign(-=):",b)
b*=10
print("Multiply and assign(*=):",b)
b**=10
print("Exponentiate and assign(**=):",b)
b/=10
print("Divide and assign:(/=)",b)
b//=10
print("Floor Divide and assign:(//=)",b)
b%=10
print("Modulus and assign:(%=)",b)
print()
# Add and assign(+=): 50
# Subract and assign(-=): 40
#  Multiply and assign(*=): 400
# Exponentiate and assign(**=): 104857600000000000000000000
# Divide and assign:(/=) 1.048576e+25
# Floor Divide and assign:(//=) 1.048576e+24
# Modulus and assign:(%=) 0.0

## Logical operators
print("Logical operators")
x=30
y=10
print("and:",(x%10==0)and (y%10==0))
print("OR:",(x%10==0)or (y%10==0))
print("not:",not (x%10==0))
# and: True
# OR: True
# not: False 
print()
## Membership Operators
print("Membership Operatord")
names=["Venkat","Naga","Raghav","Mohitananda","Sanjay"]
print("in result :","Sharma" in names)
print("not in result :","Radhakrishna" not in names)
# in result : False
# not in result : True
print()
## Identity operators 
print("Identity Operators:")
x=[1,2,4,5]
y=[1,2,4,5]
print("x is y :",x is y)
z=x 
print("z is x :",z is x)
print("id(x):",id(x))
print("id(y):",id(y))
print("id(z):",id(z))
print("z is not x: ",z is not x)
print("z is not y: ",z is not y)
# x is y : False
# z is x : True
# id(x): 2110804840704
# id(y): 2110806704064
# id(z): 2110804840704
# z is not x:  False
# z is not y:  True
print()
## Bitwise operators 
print("Bitwise Operators:")
print("and operator 3 & 5:",3&5)
print("or operator  4 | 5:",4|5)
print("xor operator 5 ^ 6:",5^6)
print("~1 not operator : ",~1)
print("left shift operator by   1 bit 4<<1: ",2<<1)#Multiply by 2
print("left shift operator by   2 bit 4<<2: ",4<<2)
print("right shift operator by  1 bit 4>>1: ",4>>1)# Divide by 2
print("right shift operator by  2 bit 4>>2: ",4>>2)
# and operator 3 & 5: 1
# or operator  4 | 5: 5
# xor operator 5 ^ 6: 3
# ~1 not operator   :  -2
# left shift operator by   1 bit 4<<1:  4
# left shift operator by   2 bit 4<<2:  16
# right shift operator by  1 bit 4>>1:  2
# right shift operator by  2 bit 4>>2:  1