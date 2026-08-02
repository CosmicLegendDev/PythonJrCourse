# Print the elements in a list in reverse order.
# i.e. [1, 2, 3, 4, 5, 6]
# op: 6 5 4 3 2 1

numbers = [1, 2, 3, 4, 5, 6 ,7, 8]
numbers_size = len(numbers)
print(numbers_size)
print(5 * "*" + " Item in reverse order " + 5 * "*")
for i in range(numbers_size - 1, -1, -1):
    print(numbers[i])
