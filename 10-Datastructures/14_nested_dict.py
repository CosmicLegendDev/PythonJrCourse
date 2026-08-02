# Nested dictionary.
biodata = {
    "Father": {
        "Name": "Kanthan",
        "Age": 38,
        "Address": "America"
    },
    "Mother": {
        "Name": "Some name",
        "Age": 34,
        "Address": "America"
    }
}

# Print father details.
father_dict = biodata["Father"]
print(f"Name: {father_dict.get('Name')} Age: {father_dict.get('Age')}")