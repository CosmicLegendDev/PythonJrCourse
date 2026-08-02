# Write a program which can allow me to enter person biodata in a loop until I say exit.

can_proceed = True

while(can_proceed):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")

    print("-" * 20)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")
    print("-" * 20)
    choice = input("You want input another biodata (Y/N)?")
    if choice == 'N':
        can_proceed = False
    else:
        can_proceed = True

# Write a program to perform multiple additional operations until
#  I say exit.
# First Nmber: 2
# Second Number: 3
# Total: 5
# You want to continue? Y
# First Number: 4
# Second NUmbe: 5
# Total: 9
# You want to contune? N


