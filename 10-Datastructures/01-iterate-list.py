# Iterations, means looping over elements in the list.
# [a, b, c, d, e], iteration means accessing each and every element in the list using the loops.

cities = ["Newyork", "Newjersey", "Florida", "Pioria", "Losangels", "Chicago", "Sanfrancisco"]

print(5 * "*" + " My Favorite citiex " + 5 * "*")
for i in range(0, 6, 1): # Here we hard coded the length of the elements, 
                         #but in realtime we might not be knowing it as the list is dynamic.
    print(cities[i])

# For dynamic lists, we can use len() built in func to get the size of the list.
# First: get the length, and use for loop to iterate.
cities_size = len(cities)
print(5 * "*" + " Print citieis with dynamic size " + 5 * "*")
print(f"Cities size is {cities_size}")

for i in range(0, cities_size, 1):
    print(cities[i])