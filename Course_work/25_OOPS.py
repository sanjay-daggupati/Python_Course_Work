"""class Details:
    def __init__ (self,name,mail,pwd):
        self.name=name
        self._mail=mail
        self.__pwd=pwd
    def getpassword(self):#getter
        return self.__pwd 
    def setpassword(self,newpassword):#setter
        self.__pwd=newpassword
Sanjay=Details("Sanjay","sanjay@gmail.com","Sanjay@123")
print(Sanjay.name)
Sanjay.name="Raghava"
print(Sanjay.name)
print(Sanjay._mail)
Sanjay._mail="raghava123@gmail.com"
print(Sanjay._mail)
print(Sanjay.getpassword())
Sanjay.setpassword("1234@123")
print(Sanjay.getpassword())
#print(Sanjay.__pwd) cannot be displayed because of private attribute """

class Bank:
    def __init__(self):
        self.name="xyz"
        self.__balance=0
    @property
    def display_balance(self):
        return self.__balance
    @display_balance.setter
    def display_balance(self,amount):
        self.__balance+=amount
b=Bank()
print(b.name)
print(b.display_balance)
b.display_balance=2500
print(b.display_balance)