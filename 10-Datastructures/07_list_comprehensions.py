#List Comprehensions, simplified code to do some operations on the list.

# Find squres of each element in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    print(i * i)

squares_of_numbers = [i*i for i in numbers]
print(type(squares_of_numbers))
print(f"Squares with comprehensive operation: {squares_of_numbers}")

# Using comprehensive operation, find even numbers in a list.

even_numbers = [i for i in numbers if i % 2 == 0]
print(f"Event numbers using comprehensive ops: {even_numbers}")

