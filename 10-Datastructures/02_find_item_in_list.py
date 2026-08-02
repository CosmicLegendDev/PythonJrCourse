# Find an element in a list by iterating the list. 
# Searching an element in a list/array.

cities = ["Chicago", "Sanfransisco", "Losangels", "Piorio", "Cincinatti", "Newjersey"]

# find an element "Newjersey"

# step 1: get the size of the list.
cities_size = len(cities)

# step 2: declare a variable to hold the desired item.
desired_city = "Newjersey"

# step 3: iterate the list and compare items with desired_city
found = False # set to false, if found turn to True.
for i in range(0, cities_size, 1):
    if desired_city == cities[i]:
        found = True

# Step 4: Check if found is True, if yes print found the element, else Print Element not found.
if found:
    print("Item Found in a list.")
else:
    print("Item Not found in a list.")



# Write a program to find as item in a list, 
# and the progrm should be able to find item 
# irrespective of the case (camel case, mixed case..).
