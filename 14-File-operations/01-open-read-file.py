# Open and Read file data.

my_file = open("/Users/durgalovababupadala/Downloads/sample_file.rtf", "r")
content = my_file.readlines()
print("File content:", content)
my_file.close()
