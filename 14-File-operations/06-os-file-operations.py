# File advance operations using os module.

import os

# File exist or not
if os.path.exists("my_bio1.txt"):
    print("File exist.")
else:
    print("File not exist, hence creating a file now...")
    file = open("my_bio1.txt", "w")
    file.write("File created successfully by Phton.")
    file.close()

os.rename("my_bio1.txt", "my_bio2.txt")

os.remove("my_bio2.txt")


