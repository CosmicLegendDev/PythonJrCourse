# Function with return type.

# def <func_name>(<...>):
#    return <value>

# function to add two numbers and return sum.

def add(a, b):
    res = a + b
    print(f"sum of a, b is {res}")
    return res # exit.

ret_val = add(3, 4)
print(ret_val)

