# Strings in Python

Strings are sequences of characters enclosed in either single quotes (' ') or double quotes (" "). They are used to represent text in Python.
Ex. ```python

# Using single quotes

string1 = 'Hello, World!'

# Using double quotes

string2 = "Hello, World!"

````
## String Concatenation
String concatenation is the process of combining two or more strings into one. In Python, you can concatenate strings using the `+` operator.
Ex. ```python
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)  # Output: Hello World
````

## String Formatting

String formatting allows you to create a new string by inserting values into a template string. In Python, you can use the `format()` method or f-strings for string formatting.
Ex. ```python
name = "Alice"
age = 30  
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

````
## String Methods
Python provides a variety of built-in string methods that allow you to manipulate and work with strings. Some common string methods include:
- `lower()`: Converts all characters in the string to lowercase.
- `upper()`: Converts all characters in the string to uppercase.
- `strip()`: Removes leading and trailing whitespace from the string.
- `split()`: Splits the string into a list of substrings based on a specified delimiter.
- `replace()`: Replaces occurrences of a specified substring with another substring.
Ex. ```python
text = "  Hello, World!  "
print(text.lower())        # Output: "  hello, world!  "
print(text.upper())        # Output: "  HELLO, WORLD!  "
print(text.strip())        # Output: "Hello, World!"
print(text.split(", "))    # Output: ['  Hello', 'World!  ']
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "
````

## String Slicing

String slicing allows you to extract a portion of a string by specifying a range of indices. The syntax for string slicing is `string[start:end]`, where `start` is the index of the first character to include and `end` is the index of the first character to exclude.
Ex. ```python
text = "Hello, World!"
print(text[0:5]) # Output: "Hello"
print(text[7:12]) # Output: "World"

````
# How slice works with negative values?
When you use negative values in string slicing, it counts from the end of the string instead of the beginning. The index `-1` refers to the last character, `-2` refers to the second-to-last character, and so on.
Ex. ```python
text = "Hello, World!"
print(text[-6:-1]) # Output: "World"

````

# String Immutability

In Python, strings are immutable, which means that once a string is created, it cannot be modified. Any operation that seems to modify a string actually creates a new string.

Ex. ```python
text = "Hello"
new_text = text + " World"
print(text) # Output: "Hello"
print(new_text) # Output: "Hello World"

```

```
