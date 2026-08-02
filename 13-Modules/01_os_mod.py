# Operating System module.

import os

path = os.environ.get("CLASS_NAME")
print(path)

print(os.getcwd()) #cwd means current working directory.

os.chdir(path="/Users")

print(os.getcwd())
