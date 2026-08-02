# Practive methods in string.

# lower()
name = "GuhaN"
lower_name = name.lower()
print(lower_name)

# upper()
name = "GuhaN"
upper_name = name.upper()
print(upper_name)

# strip() - remove the trailing spaces
name = "Guhan "
strip_name = name.strip()
print(name)
print(len(name))
print(strip_name)
print(len(strip_name))

# split() - splits the string using delimeter character.
name = "Guhan-Kaanthan-Latchiya"
split_names = name.split("-") # ["Guhan", "Kanthan", ".."]
print(split_names)

# startswith("") - return true if string start with supplied string, else returns false. 
is_start_with = name.startswith("Guh")
print(is_start_with)

# endswith() - return true if the string end with supplied string, else return false.
is_end_width = name.endswith("ya")


city = "america"
print(city.capitalize())

name = "Guhan"
print(name.casefold())

join_str = " ".join(["Hello", "World", "Welcome to Python."])
print(join_str)








