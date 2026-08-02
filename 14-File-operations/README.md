# File Operations in Python.

## What is a file?

File is a named location on the disk to store data. It can be a text file, binary file, or any other type of file.

## File Operations

Python provides several built-in functions to perform file operations. Some of the common file operations are:

1. Open a file
2. Read from a file
3. Write to a file
4. Append to a file
5. Close a file

### 1. Open a file

To open a file, we use the `open()` function. The syntax is:

```python
file = open('filename', 'mode')
# mode can be 'r' for read, 'w' for write, 'a' for append, etc.
# filename is the name of the file you want to open.
```

### 2. Read from a file

To read from a file, we can use the `read()`, `readline()`, or `readlines()` methods. For example:

```pythonfile = open('example.txt', 'r')
content = file.read()  # Reads the entire file
print(content)
file.close()
```

### 3. Write to a file

To write to a file, we can use the `write()` method. For example:

```python
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
```

### 4. Append to a file

To append to a file, we can use the `append` mode. For example:

```python
file = open('example.txt', 'a')
file.write('\nThis is an appended line.')
file.close()
```

### 5. Close a file

It is important to close a file after performing operations on it to free up system resources. We can use the `close()` method to close a file. For example:

```python
file = open('example.txt', 'r')
# Perform file operations
file.close()
```

Alternatively, we can use the `with` statement to automatically close the file after the block of code is executed:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

This way, we don't have to worry about closing the file manually.

### Advanced file operations.

Python also provides other file operations such as checking if a file exists, deleting a file, and renaming a file using the `os` module. For example:

```python
import os
# Check if a file exists
if os.path.exists('example.txt'):
    print('File exists')
else:
    print('File does not exist')

# Delete a file
os.remove('example.txt')
# Rename a file
os.rename('old_name.txt', 'new_name.txt')
```

### File seek operation

The `seek()` method is used to change the file's current position. The syntax is:

```python
file = open('example.txt', 'r')
file.seek(0)  # Move to the beginning of the file
content = file.read()
print(content)
file.close()
```

# Home work.

## Create a Python program to write entire your family members bio data in a text file and read the data from the file and display it on the console.

## Create a interactive program which should ask for the user to enter the name of the file and then ask for the content to write in that file. After writing, it should read the content from the file and display it on the console.
