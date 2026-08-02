# creating a set
# Characterstics of set, 
# - It wont allow duplicate
# - Set is not index based as like list.
# - Set is dynamic, you can add any number of elements.
# - Set is declared using curly braces {}
# - Order of insertion is not guaranteed.

subjects = {"Maths", "Science", "Social"} # set is not indexed, and no guarantee of order of insertion.
print(subjects)

subjects.add("English") # it adds element to the set, order is unknown.
print(subjects)

subjects.add("Engineering")
print(subjects)

pop_ele_1 = subjects.pop() # it takes top element from set, and it deleted.
print(pop_ele_1)
print(subjects)

pop_ele_2 = subjects.pop() # it takes top element from set, and it deleted.
print(pop_ele_2)
print(subjects)

