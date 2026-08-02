# creating a list.
subjects = ["Maths", "Science", "Computers"] # ordered, index based linear data structure.
print(type(subjects))
print(subjects)

# Accessing elements from List. i.e. variable_name[index]
print(subjects[0])
print(subjects[1])
print(subjects[2])
# print(subjects[3])  # throws index error because 3rd index not present list.

# Putting element to the list at the posion 2.
subjects[2]="Social" 
print(subjects[2])
print(subjects)

# Removing element by element from the list.
subjects.remove("Science")
print(subjects)

# Expanding the list by adding additional elements.
subjects.append("Engineering")
subjects.append("Maths") # list allows duplicate
print(subjects)
print(subjects[3])

# Removes all the elements from the list.
subjects.clear()
print(subjects)

# Inserts the element before the index specified.
# It re-arranges the elements in the list.
subjects.insert(0, "Maths")
print(subjects)
print(subjects[0])

subjects.insert(2, "Science")
print(subjects)
print(subjects[1])

subjects.insert(1, "Social")
print(subjects)
subjects.insert(1, "Computers")
print(subjects)

# index is the method returns the first index of the element in the list.
social_index = subjects.index("Social")
print(social_index)

#bilogy_index = subjects.index("Biology")
#print(bilogy_index)

subjects.append("Social")
print(subjects)

social_index = subjects.index("Social")
print(social_index)

social_index = subjects.index("Social", 3)
print(social_index)

# count() method returns the number of occurances 
subjects.append("Social")
count_of_social = subjects.count("Social")
print(count_of_social)

# It reverse the entire index, first element will become last element.
subjects.reverse()
print(subjects)

# extends the existing list with additional list provided.
subjects.extend(["Biology", "EVS"])
print(subjects)


# Create a list of subjects, 
# and find the index of subject "Social", 
# and replace it with GeneralKnowledge.










