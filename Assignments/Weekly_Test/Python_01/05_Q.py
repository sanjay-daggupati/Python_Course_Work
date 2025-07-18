credentials=("admin","python123")
username=input()
password=input()
if(username==credentials[0] and password==credentials[1]):
    print("Login Sucessful")
else:
    print("Access denied")
# admin 
# python123
# Login Sucessful
# admin 
# python163
# Access denied
