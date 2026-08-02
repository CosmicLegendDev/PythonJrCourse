# Dictionary
mark_sheet = {
    "Maths": 99,
    "Social": 89.5,
    "English": 97,
    "Result": "Pass" 
}

print(type(mark_sheet))

# Access element from dict.
maths_marks = mark_sheet.get("Maths")
print(f"Marks in maths: {maths_marks}")

# Add element to dictionary
mark_sheet["EVS"] = 95
print(mark_sheet)

dict_keys = mark_sheet.keys()
print(f"Dict keys: {dict_keys}")
print(type(dict_keys))
dict_values = mark_sheet.values()
print(f"Dict values: {dict_values}")

gk_marks = {"GK": 89}
mark_sheet.update(gk_marks)
print(mark_sheet)