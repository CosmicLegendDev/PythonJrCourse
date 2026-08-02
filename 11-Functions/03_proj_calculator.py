# User can enter two numbers with operator.

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def validate(n1, n2):
    n1_int = int(n1)
    n2_int = int(n2)
    return (n1_int, n2_int)

is_continue = True
while(is_continue):
    n1 = input("Enter First number: ")
    n2 = input("Enter Second number: ")

    numbers = validate(n1, n2)

    print("Calculator Operations: ")
    print("1. add")
    print("2. sub")
    operation = input("Choose Operation:")
    
    #validate_operator(operation)
    match(operation):
        case "1":
            res = add(n1=numbers[0], n2=numbers[1])
            print(f"Sum of {numbers[0], numbers[1]} is {res}")
        case "2":
            res = sub(n1=numbers[0], n2=numbers[1])
            print(f"Sum of {numbers[0], numbers[1]} is {res}")
        case _:
            print("Invalid operator choosen.")
    
    response = input("Do you want to continue(Y/N)?")
    if response == "N":
        is_continue = False

# Fix response capitalize issue.
# Expand the calculator to 
#  multiplication, division, modulus, percentage, square.
# add validate_operator() method.
# extract operator options to another method.
#   print_operators()