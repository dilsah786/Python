# Dictionary and Set in Python

"""
Dictionary are used to store data values in key:value pairs
They are unordered, mutable(changeable) and dont't allow duplicates

"key" : value

"""

information = {
    "name":"Dilnawaz",
    "subject":"Web Developement",
    "topics":("dictonary","set"),
    "marks":[98,95,69],
    "age":22,
    "is_Adult":True
}

# print(information)
print(information["name"])
print(information["subject"])
print(information["marks"])
print(type(information))

# update value of name and add a new key value to information

information["name"] = "Md Dilnawaz"
information["surname"] = "Alam"

print(information["surname"])

# Nested dictionary

student = {
    "name":"Dilsah",
    "subject" :{
        "Physics":98,
        "Chemistry":96,
        "Biology":95,
        "Math":82
    }
}

print(student["subject"]["Math"])

# Dictionary Methods

"""
myDict.keys()   ----> returns all keys

myDict.values()  -----> returns all values

myDict.items()   -----> returns all (key,val) pairs as tuples

myDict.get("key") -----> returns the key according to value

myDict.update(newDict) -----> inserts the specified items to the dictionary

"""

print(student.get("name"))


# Set in Python
"""
Set is the collection of the unordered items.
Each element in the set must be unique and immutable


set = set()   # empty set syntax

nums = {1,2,3,4}
set1 = {1,2,2,1}

repeated elements stored only once , so it resolved ot {1,2}

"""
# Set Methods 
"""
set.add(el) --------> adds an element

set.remove(el)  -------> removes the element

set.clear()   -------> empties the set

set.pop()   ----------> removes a random value

set.union(set2)  ----------> combines both set values and returns a new set

set.intersection(set2)  ---------> combines common element and return as new set 

"""
newSet = set()

newSet.add(10)
newSet.add(9)
newSet.add(8)
newSet.add(8)
newSet.add(9)
newSet.add(5)
newSet.add("el") 

print(newSet)
newSet.pop()
newSet.add(5)
print(newSet)
(newSet.remove(5))
print(newSet)
0
newSet.clear()
print(len(newSet))



set1 = {1,2,3,4,5,6,7,8,9,7}
set2 = {5,6,7,8,1,3,4,9,6,10,46,}

ans_union = set1.union(set2)

ans_intersection = set1.intersection(set2)



print("ans_union ", ans_union)

print("ans_intersection ", ans_intersection )


# Let's Practice

"""
Question-1 : 

Store following word meaning in a python dictionary
tabel : "a piece of furniture" , "list of facts & figures1"
cat : "a small animal"


Questions 2 : 

You are given a lists of subjects for students.
 Assume one classroom is required for 1 subject. How many classroom are needed by all students

 "python","java","c++","javaScript","java","python","java","c++","c" 


 Question 3 :

 WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start an empty dictionary and add one by one. 
 Use subject name as key marks as value.




 Question -4 :

 Figure out a way to store 9 and 9.0 as seperate values in the set
 (You can take help of built-in-data types)









"""


# Ans -1

dictionary  = {
    "table":["a piece of furniture","lists of facts & figurees"],
    "cat":"a small animal"
}

print(dictionary)


# Ans-2

student={
    "python","java","c++","javaScript","java","python","java","c++","c" 
}

print(len(student))

# Ans - 3

# physics = int(input("Enter Physics marks : "))
# Chemistry = int(input("Enter Chemistry marks : "))
# Math = int(input("Enter Math marks : "))


# Subjects_Marks = {}

# Subjects_Marks.update({"physics": physics})
# Subjects_Marks.update({"Chemistry": Chemistry})
# Subjects_Marks.update({"Math":Math})

# print(Subjects_Marks)

# Ans -4

store = {
    9,"9.0"
}


print(store)