# Data Types in Python

Python has several built-in data types that are used to store different kinds of data. Here are some of the most commonly used data types:

1. **Integer (`int`)**: Represents whole numbers, both positive and negative.
   ```python
   age = 25
   ```
2. **Floating Point (`float`)**: Represents real numbers with decimal points.
   ```python
   height = 5.9
   ```
3. **String (`str`)**: Represents sequences of characters, enclosed in single or double quotes.
   ```python
   name = "Alice"
   ```
4. **Boolean (`bool`)**: Represents truth values, either `True` or `False`.
   ```python
   is_student = True
   ```

# Type casting

Type casting is the process of converting one data type to another. In Python, you can use built-in functions to perform type casting:

```python
# Converting float to integer
float_number = 10.7
int_number = int(float_number)  # Result: 10

age = "25"
int_age = int(age)  # Result: 25

i = 10
float_i = float(i)  # Result: 10.0

a = "a"
int_a = int(a)  # This will raise a ValueError
```
