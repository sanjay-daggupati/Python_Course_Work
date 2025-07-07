a={1,2,3,4}
print(type(a))
empty_set=set()
print(type(empty_set))
b={1,2,3,4,2,4,3}
print(b)
# Lists are mutable and cannot be added to a set
print(3 in a)
print(5 not in b)
a={1,2,3,4,5,6}
b={2,4,6}
print(f"Union {a | b}")
print(f"Intersection {a&b}")
print(f"Difference {a-b}")
print(f"Symmetric_differnce {a^b}")
print(f"issubset {b<=a}")
print(f"issuperset {a>=b}")
a={1,2,3}
b={4,5,6}
print(f"isdisjoint {a.isdisjoint(b)}")
print("built in methods")
a={1,2,3,4,5,6}
a.add(7)
print(a)
a.remove(5)#Removes an element; raises anerror if the element doesn’t exist
print(a)
a.discard(9)
print(a)
a.pop()
print(a)
a={1,2,3,4,5,6,7}
b={1,4,9,11}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
a.update(b)
b.intersection_update(a)
a.difference_update(b)
a.symmetric_difference_update(b)
d={1,2,3,4,56,7,}
c=d.copy()
print(c)
print(len(c))
print(max(c))
print(min(c))
print(sum(c))
print(sorted(c))
print(set("Sanjay"))
print("Frozen set")
frozen=frozenset([1,2,3,4])
print(frozen)