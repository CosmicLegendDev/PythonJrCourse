# Printing age group.
# if age is between 0-13, you are a kid.
# if age is between 13-20, you are a teenager
# if age is between 20-30, you are a younger.
# if age is above 30, you are a adult.
print("*" * 10, " Age Group finder " , "*" * 10)

age = int(input("Enter your age: "))

# if age between 0 - 13, kid
if age < 13:
    print("You are a kid.")
elif age > 13 and age < 20: # if age between 13-20
    print("You are teenager.")
elif age > 20 and age < 30: # if age between 20-30
    print("You are a younger.")
else:
    print("You are an adult.")
