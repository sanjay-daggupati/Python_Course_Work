a=()
print(type(a))
b=(5,)
print(b)
c=(1,"apple",3.5)
print(c)
d=1,2,3
print(d)
a=(20,30,40,50)
print(a[2])
print(a[-2])
print(a[1:4])
b=(1,2)
c=(3,4)
d=b+c
print(d)
print(b*3)
print(2 in d)
print(5 not in d)
f=(1,2,3)
a,b,c=f
print(a,b,c)
a=(1,2,1,2,3)
print(f"Count:{a.count(1)}")
print(f"index:{a.index(2)}")
print(f"Length {len(a)}")
print(f"Maximum:{max(a)}")
print(f"Minimum:{min(a)}")
print(f"Sum:{sum(a)}")
print(tuple[1,2,3])
print(tuple("Sanjay"))
nested=[1,[1,2]]
print(nested[1][0])
# <class 'tuple'>
# (5,)
# (1, 'apple', 3.5)
# (1, 2, 3)
# 40
# 40
# (30, 40, 50)
# (1, 2, 3, 4)
# (1, 2, 1, 2, 1, 2)
# True
# True
# 1 2 3
# Count:2
# index:1
# Length 5
# Maximum:3
# Minimum:1
# Sum:9
# tuple[1, 2, 3]
# ('S', 'a', 'n', 'j', 'a', 'y')
# 1