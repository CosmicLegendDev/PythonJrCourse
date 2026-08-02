# String formatting in Python

String formatting is a way to create formatted strings by embedding variables or expressions within string literals. Python provides several methods for string formatting, including the `format()` method and f-strings (formatted string literals).

i.e. "MY name is Guhan, and I am 12 years boy."

name = "Guhan"
age = 12

# Using the format() method

formatted_string1 = "My name is {}, and I am {} years old.".format(name, age)
print(formatted_string1)

# Using f-strings (available in Python 3.6 and later)

formatted_string2 = f"My name is {name}, and I am {age} years old."
print(formatted_string2)
