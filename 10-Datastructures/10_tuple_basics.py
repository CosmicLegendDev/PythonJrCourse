# Tuple is a immutable data structure.

my_tuple = (1, 3.5, "Hello", 3.5)
print(type(my_tuple))
# my_tuple[1] = 4 -> You cannot change, since it is immutable.

# Access element from tuple
print(f"first element in tuple: {my_tuple[0]}")

# Count of the elements in tuple
print(f"count of elements: {my_tuple.count(3.5)}")

print(f"Index of element: {my_tuple.index('Hello')}")

my_num = (1, 3, 4, 5)
print(max(my_num))
print(min(my_num))