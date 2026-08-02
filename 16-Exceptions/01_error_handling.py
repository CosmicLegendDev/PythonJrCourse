age = input("Enter your age: ")

try:
    # try block, code is getting executed.
    age_int = int(age)
    if age_int > 18:
        print("Adult.")
    else:
        print("You are a kid still.")
except ValueError as ve:
    # catch block, where errors caught.
    print("You entered invalid age, please enter a valid Number.")
