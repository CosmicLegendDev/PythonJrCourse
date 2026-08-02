# Loops in python.

Loops are used to execute a block of code repeatedly.

# Range() function.

Range() is used to generate a sequence of numbers. It can take one, two, or three arguments:

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
range(10) generates numbers from 0 to 9. Here 10 is excluded.

## Syntax of range() function:

- **range(stop)**: Generates numbers from 0 to stop-1.
  Example: range(10) - > 0 1 2 3 4 5 6 7 8 9
- **range(start, stop)**: Generates numbers from start to stop-1.
  Example: range(1, 10) - > 1 2 3 4 5 6 7 8 9
- **range(start, stop, step)**: Generates numbers from start to stop-1, incrementing by step.
  Example: range(1, 10, 2) - > 1 3 5 7 9
  Example: range(10, 0, -1) - > 10 9 8 7 6 5 4 3 2 1

## Types of loops in Python

1. **for loop**: Used to iterate a block of code in N number of times.

- Loop has a condition to break the execution.
- **Range** returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

  Example:

```python
for i in range(5): # 0 1 2 3 4
    print(i)
```

2. **while loop**: Repeats a block of code as long as a condition is true.

Example:

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

## Loop control statements

- **break**: Exits the loop.
- **continue**: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
- **pass**: Does nothing, acts as a placeholder.

Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
