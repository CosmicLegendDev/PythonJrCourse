# function with kwargs.  
# Keyword arguements, 
# function with kwargs accepts arbitrary number of named/keyword
# kwargs

def sample_args(name, age, *args):
    print(type(args))
    print(args)
    print(f"My name is {name}, and am {age}yrs old.")

sample_args("Guhan", 12, "USA", 1, 2, 4, 5)

def biodata(name, **kwargs):
    print(type(kwargs))
    print(name)
    print(kwargs)

biodata("Guhan", age=12, address="USA")

