# Seek file operation.

my_bio_file = open("my_bio.txt", "r")
content = my_bio_file.read()
print("*" * 5 + " First time read.....")
print(content)
my_bio_file.seek(49)
content = my_bio_file.read()
print("*" * 5 + " Second time read.....")
print(content)
