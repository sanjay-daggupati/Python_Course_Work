a=[]
print(type(a))
b=list()
print(type(b))
a=[1,"Sanjay",1.43,True]
print(a)
print(type(a))
print(a[2])
a.append(10)
print(a)
print(f"nested_list {[[1,2,3],["a","b","c"],[True,False]]}")
a=[10,20,30,40,50]
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[-3:-1])
print(a[::-1])
a[2]=100
print(a)
a.extend([60,70,80,90])
print(a)
a.insert(1,15)
print(a)
## Removing Elements 
print(a.remove(20))
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
del a[1]
print(a)
a=[70,30,20,100]
print()
a.sort()
print(a)
a=[70,30,20,100]
a.sort(reverse=True)
print(a)
print()
a = [70, 30, 20, 100]
b = sorted(a)
print(b)
b = sorted(a, reverse=True)
print(b)  
print("list.sort() → sorts in place, returns None.")
print("sorted() → returns a new sorted list")
a=[10,20,10,20,10]
print(a.count(10))
b=a.copy()
print(b)
a.clear()
print(a)
a=[5,3,7,8]
print(a)
a.reverse()
print(a)
a=[10,20,30,50,60,50,60]
print(a)
print(a.index(50,2,len(a)))
print("Maximum",max([10,20,30,50]))
print("Minimum",min([10,20,30,50]))
print("Sum",sum([10,20,30,50]))
print(len(a))
roll_nos=["Sanjay","Raghava","Mohitananda"]
for roll_no in roll_nos:
    print(roll_no)
for index,roll_nos in enumerate(roll_nos):
    print(index,roll_nos)
a=[{},[],(),None,"string"]
print(a)
print(any(a))
print(all(a))
a=["Sanjay","String","Python"]
print(a)
print(any(a))
print(all(a))

# <class 'list'>
# <class 'list'>
# [1, 'Sanjay', 1.43, True]
# <class 'list'>
# 1.43
# [1, 'Sanjay', 1.43, True, 10]
# nested_list [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
# [20, 30, 40]
# [10, 20, 30]
# [30, 40, 50]
# [30, 40]
# [50, 40, 30, 20, 10]
# [10, 20, 100, 40, 50]
# [10, 20, 100, 40, 50, 60, 70, 80, 90]
# [10, 15, 20, 100, 40, 50, 60, 70, 80, 90]
# None
# [10, 15, 100, 40, 50, 60, 70, 80, 90]
# [10, 15, 100, 40, 50, 60, 70, 80]
# [10, 15, 40, 50, 60, 70, 80]
# [10, 40, 50, 60, 70, 80]

# [20, 30, 70, 100]
# [100, 70, 30, 20]

# [20, 30, 70, 100]
# [100, 70, 30, 20]
# list.sort() → sorts in place, returns None.
# sorted() → returns a new sorted list
# 3
# [10, 20, 10, 20, 10]
# []
# [5, 3, 7, 8]
# [8, 7, 3, 5]
# [10, 20, 30, 50, 60, 50, 60]
# 3
# Maximum 50
# Minimum 10
# Sum 110
# 7
# Sanjay
# Raghava
# Mohitananda
# 0 Sanjay
# 1 Raghava
# 2 Mohitananda
# [{}, [], (), None, 'string']
# True
# False
# ['Sanjay', 'String', 'Python']
# True
# True