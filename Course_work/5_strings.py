s="DaggupatiVenkataNagaRaghavaMohitanandaSanjay"
print(len(s))   
print(s[12])
print(s[0:9])
print(s[9:16])
print(s[16:20])
print(s[20:27])
print(s[27:32])
print(s[32:38])
print(s[38:44])
print(s[44:37:-1])
print(s[::-1])
print(s[-6:])
print(s[-44:-35])
print(s[-36:-45:-1])
print(s[-7:-13:-1])
print(s[15:8:-1])
print(s[9])
print(s[0:44:2])
print(s[1:44:2])
a="Hello"
b="World "
print(a+" "+b)
print("Python"*3)
print("P"in "Python")
print(len("Python"))
print(max("abcXYZ"))
print(min("abcXYZ"))
print(sorted("python"))
print(ord("A"))
print(chr(97))
a="Hello"
print(f"upper():{a.upper()}")
print(f"lower():{a.lower()}")
print(f"capitalize():{a.capitalize()}")
print(f"title():{a.title()}")
print(f"swapcase():{a.swapcase()}")
print(f"casefold():{a.casefold()}")
print("Alignment & Formatting methods")
b="Krupal"
b=b.center(10,"^")
print(f"{b} :len{len(b)}")
b="Sanjay"
print(f"ljust:{b.ljust(10,"-")}")
print(f"rjust:{b.rjust(10,"-")}")
b="1"
print(f"zfill():{b.zfill(5)}")
print("Name:{} \n Age:{}".format("Tom",25))
print("{name} is {age}".format_map({"name":"Sanjay","age":"21"}))
print()
print("Search & Find Methods")
print(f"find :{"hello".find("l")}")
print(f"rfind :{"hello".rfind("r")}")
print(f"index :{"hello".index("l")}")#Like find(), but raises an error if not found.
#print(f"rfind :{"hello".rfind(1)}")#Like rfind(), but raises an error if not found.
print("hello".count("l"))
print()
print("String Testing Methods(Boolean Results)")
print(f"startswith {"python".startswith("py")}")
print(f"endswith {"Python".endswith("on")}")
print(f"isalpha() {"Python".isalpha()}")
print(f"islower() {"python".islower()}")
print(f"isupper() {"PYTHON".isupper()}")
print(f"isspace() {" ".isspace()}")
print(f"istitle() {"Hello World".istitle()}")
print(f"isidentifier() {"Variable1".isidentifier()}")
print(f"isdecimal()123 {"123".isdecimal()}")
print(f"isdigit() 123 {"123".isdecimal()}")
print(f"isnumeric() 123 {"123".isnumeric()}")
print(f"isdecimal() {'٣'.isdecimal()}")#Arabic-Indic digit
print(f"isdigit() ٣ {'٣'.isdigit()}")#Arabic-Indic digit
print(f"isnumeric() ٣ {'٣'.isnumeric()}")#Arabic-Indic digit
print(f"isdecimal() '2' {'2'.isdecimal()}")
print(f"isdigit()'2' {'2'.isdigit()}")
print(f"isnumeric() '2' {'2'.isnumeric()}")
print(f"isdecimal() '½' {'½'.isdecimal()}")
print(f"isdigit() ''½' {'½'.isdigit()}")
print(f"isnumeric() '½' {'½'.isnumeric()}")
print(f"isdigit() 'VIII' {'Ⅷ'.isdigit()}")
print(f"isdecimal() 'VIII' {'Ⅷ'.isdecimal()}")
print(f"isnumeric() 'VIII'  {'Ⅷ'.isnumeric()}")
print(f"isdigit() '12.3' {'12.3'.isdigit()}")
print(f"isdecimal() '12.3' {'12.3'.isdecimal()}")
print(f"isnumeric() '12.3' {'12.3'.isnumeric()}")
print("Replace & Modify")
print(f"replace()(old,new){"apple".replace("p","b")}")
print(f"maketrans() {"Orange".maketrans("hnge","#5m8")}")
print(f"translate() {"Orange".translate(str.maketrans("hnge","#5m8"))}")
print("Splitting & Joining Methods")
print("Venkata,Naga,Raghava".split(","))
print("Venkata,Naga,Raghava".rsplit(",",1))
print("Venkata\nNagaRaghava".splitlines())
print(" ".join(["Venkata","Naga"]))
print("chesse-cake-by-Sanjay".partition("-"))
print("chesse-cake-by-Sanjay".rpartition("-"))
print("WhiteSpace & Trimming Methods")
print(" hello ".strip())
print("---Sanjay".lstrip("-"))
print("Sanjay****".rstrip("*"))
print("Encoding & Decoding ")
print("hello".encode("utf-8"))
print("😂😂❤️".encode("utf-8"))
print(b'\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xe2\x9d\xa4\xef\xb8\x8f'.decode("utf-8"))
print(b'hello'.decode("utf-8"))
44
# k
# Daggupati
# Venkata
# Naga
# Raghava
# Mohit
# ananda
# Sanjay
# yajnaS
# yajnaSadnanatihoMavahgaRagaNatakneVitapuggaD
# Sanjay
# Daggupati
# itapuggaD
# adnana
# atakneV
# V
# DguaiektNgRgaaoiaadSna
# agptVnaaaaahvMhtnnaajy
# Hello World
# PythonPythonPython
# True
# 6
# c
# X
# ['h', 'n', 'o', 'p', 't', 'y']
# 65
# a
# upper():HELLO
# lower():hello
# capitalize():Hello
# title():Hello
# swapcase():hELLO
# casefold():hello
# Alignment & Formatting methods
# ^^Krupal^^ :len10
# ljust:Sanjay----
# rjust:----Sanjay
# zfill():00001
# Name:Tom
#  Age:25
# Sanjay is 21

# Search & Find Methods
# find :2
# rfind :-1
# index :2
# 2

# String Testing Methods(Boolean Results)
# startswith True
# endswith True
# isalpha() True
# islower() True
# isupper() True
# isspace() True
# istitle() True
# isidentifier() True
# isdecimal()123 True
# isdigit() 123 True
# isnumeric() 123 True
# isdecimal() True
# isdigit() ٣ True
# isnumeric() ٣ True
# isdecimal() '2' True
# isdigit()'2' True
# isnumeric() '2' True
# isdecimal() '½' False
# isdigit() ''½' False
# isnumeric() '½' True
# isdigit() 'VIII' False
# isdecimal() 'VIII' False
# isnumeric() 'VIII'  True
# isdigit() '12.3' False
# isdecimal() '12.3' False
# isnumeric() '12.3' False
# Replace & Modify
# replace()(old,new)abble
# maketrans() {104: 35, 110: 53, 103: 109, 101: 56}
# translate() Ora5m8
# Splitting & Joining Methods
# ['Venkata', 'Naga', 'Raghava']
# ['Venkata,Naga', 'Raghava']
# ['Venkata', 'NagaRaghava']
# Venkata Naga
# ('chesse', '-', 'cake-by-Sanjay')
# ('chesse-cake-by', '-', 'Sanjay')
# WhiteSpace & Trimming Methods
# hello
# Sanjay
# Sanjay
# Encoding & Decoding
# b'hello'
# b'\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xe2\x9d\xa4\xef\xb8\x8f'       
# 😂😂❤️
# hello