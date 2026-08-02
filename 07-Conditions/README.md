# Decision making statements in Python.

## Basic structure of if-elif-else code:

```
if condition:
    #if block: block of code to be executed if condition is true
elif condition2:
    #elif block: block of code to be executed if condition2 is true
else:
    #else block: block of code to be executed if both conditions are false
```

# 1. if statement

if is used to check whether condition is true or not. If condition is true, then block of code is executed otherwise it is skipped.

Example:

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

# 2. if-else statement

if-else statement is used to check whether condition is true or not. If condition is true, then block of code in if block is executed otherwise block of code in else block is executed.

Example:

```python
age = 19
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

# 3. if-elif-else statement

if-elif-else statement is used to check multiple conditions. If condition in if block is true, then block of code in if block is executed. If condition in elif block is true, then block of code in elif block is executed. If both conditions are false, then block of code in else block is executed.

Example:

```python
age = 20
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

# Comparision operators:

Comparison operators are used to compare two values. The result of comparison is either true or false.

- `==` : equal to
- `!=` : not equal to
- `>` : greater than
- `<` : less than
- `>=` : greater than or equal to
- `<=` : less than or equal to

# Logical Operators:

Logical operators are used to combine multiple conditions. The result of logical operation is either true or false.

- `and` : returns true if both conditions are true
  if condition1 and condition2:
  True and True = True
  True and False = False
  False and True = False
  False and False = False
- `or` : returns true if at least one condition is true
  if condition1 or condition2:
  True or True = True
  True or False = True
  False or True = True
  False or False = False
- `not` : returns true if condition is false
  if not condition:
  not True = False
  not False = True

# Nested if statements:

Nested if statements are if statements inside another if statement. The inner if statement is executed only if the outer if statement is true.

Example:

```python
age = 20
if age >= 18:
    if age < 21:
        print("You are an adult but not old enough to drink alcohol in the US.")
    else:
        print("You are an adult.")
```

Write a program to check whether number is even or odd.

- read the number from Terminal using input() function.

Write a progam to check whether number is between 1 and 100 and also check whether it is even or odd.

- read the number from Terminal using input() function.

# Match statement in python

Is a control flow mechanism used for structural pattern matching.
Example:

```python
    age = 20
    match age:
        case age if age >= 18 and age < 21:
            return "You are teenager."
        case age if age >= 21:
            return "You are an adult."
        case _:
            return "You are a child."
```
