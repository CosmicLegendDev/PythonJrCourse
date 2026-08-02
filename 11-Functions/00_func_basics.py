# Define a function to greet person.

def hello(): # func with zero arguement/parameter.
    print("Hello, welcome to python.")

hello() # invoking/calling function.
hello()
hello()
hello()

def hello(name): # name is variable, and it is local to function.
    print(f"Hello, {name}. Welcome to Python")

hello("Guhan")

def hello(name, city):
    print(f"Hello {name}, Welcome to {city}")

hello("Guhan", "Newyork")
hello("Newyork", "Guhan")
hello(city="NewJersey", name="Guhan")

# Define a function which takes number as param, 
#  and print whether it is a even or odd.



