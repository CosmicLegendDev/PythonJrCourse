# sum operation.
# 1 + 1 = 2
# n1 and n2, read from console and then perform n1 + n2.
print("*" * 10 + " My Calculator " + "*" * 10)

print(9 ^ 3)


n1 = input("Enter First number: ")
n2 = input("Enter Second number: ")

int_n1 = int(n1)
int_n2 = int(n2)
sum = int_n1 + int_n2

print(f"Sum of two numbers is:{sum}")

# Subtraction
# Multiplication
# Division
print("*" * 10, " Division (/). ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
res = n1 / n2
print(f"Division of two numbers is: {res}")

# Floor division
print("*" * 10 + " Floor division (//). ")
n1 = int(input("Enter Number one: "))
n2 = int(input("Enter Number two: "))
res = n1 // n2
print(f"Floor division result is: {res}")

# Modulus %
print("*" * 10 + " Modulus (%). ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
res = n1 % n2
print(f"The modulus value is : {res}")

# Exponential
print("*" * 10 + " Exponent (**). ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
res = n1 ** n2
print(f"Exponential value is: {res}")





