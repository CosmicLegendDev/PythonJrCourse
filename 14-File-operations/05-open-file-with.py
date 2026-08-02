# Open file with 'with' statement.
# No explicit file close operation needed.

with open('my_bio.txt', 'r') as my_bio_file:
    print(my_bio_file.read())
