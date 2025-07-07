a={}
print(type(a))
a=[("name","Sanjay"),("age",21),("course","ECE")]
print(dict(a))
student={
    "name":"Sanjay",
    "age":21,
    "course":"ECE"
}
print(student["name"])
## Dictionary methods for Accessing Data
print(student.get("age"))
print(student.get("city","Not Available"))
student["city"]="Hyderabad"
student["name"]="Raghava"
print(student)
print(student.items())
print(student.keys())
print(student.values())
age=student.pop("age")
print(f"age :{age}")
print(student)
student.popitem()
print(student)
##Dictionary methods for Adding and updating data
student={
    "name":"Sanjay",
    "age":21,
    "course":"ECE",
    "city":"Hyderabad"
}
print(student)
student.update({"city":"Vijayawada"})
print(student)
student.setdefault("skills","Python")
print(student)
student.setdefault("skills","java")
print(student)
print(f"length {len(student)}")
print(f"Maximum {max(student)}")
print(f"Minimum {min(student)}")
print(f"Sorted {sorted(student)}")
# <class 'dict'>
# {'name': 'Sanjay', 'age': 21, 'course': 'ECE'}
# Sanjay
# 21
# Not Available
# {'name': 'Raghava', 'age': 21, 'course': 'ECE', 'city': 'Hyderabad'}
# dict_items([('name', 'Raghava'), ('age', 21), ('course', 'ECE'), ('city', 'Hyderabad')])
# dict_keys(['name', 'age', 'course', 'city'])
# dict_values(['Raghava', 21, 'ECE', 'Hyderabad'])
# age :21
# {'name': 'Raghava', 'course': 'ECE', 'city': 'Hyderabad'}
# {'name': 'Raghava', 'course': 'ECE'}  
# {'name': 'Sanjay', 'age': 21, 'course': 'ECE', 'city': 'Hyderabad'}
# {'name': 'Sanjay', 'age': 21, 'course': 'ECE', 'city': 'Vijayawada'}        
# {'name': 'Sanjay', 'age': 21, 'course': 'ECE', 'city': 'Vijayawada', 'skills': 'Python'}
# {'name': 'Sanjay', 'age': 21, 'course': 'ECE', 'city': 'Vijayawada', 'skills': 'Python'}
# length 5
# Maximum skills
# Minimum age
# Sorted ['age', 'city', 'course', 'name', 'skills']