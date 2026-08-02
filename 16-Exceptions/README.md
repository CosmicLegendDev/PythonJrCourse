# Exceptions in Python

In Python, exceptions are used to handle errors that occur during the execution of a program. When an error occurs, Python stops the normal flow of the program and raises an exception. You can handle exceptions using `try` and `except` blocks.

## Example

```python
try:
    x = int("a")
except ValueError:
    print("Invalid value provided. Please enter a valid integer.")
```

## Finally Block

Finally block is used to execute code regardless of whether an exception was raised or not. It is often used for cleanup actions, such as closing files or releasing resources.

```python
try:
    x = int("a")
except ValueError:
    print("Invalid value provided. Please enter a valid integer.")
finally:
    print("This block is always executed.")
```
