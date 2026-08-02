file = None
try:
    file = open("abc.txt", "r")
    print(file.readlines())
except FileNotFoundError as fe:
    print("File not exist, please create first.")
finally:
    if file:
        file.close()