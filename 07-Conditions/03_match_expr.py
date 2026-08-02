day = input("Enter day:").lower()

match day:
    case "sunday":
        print("You are on day 1 of the week.")
    case "monday":
        print("You are on day 2 of the week.")
    case _:
        print("Will do it later.")

# Write a program which can accept numbers from 1-12, and 
# print each month name by its number.
# i.e. Enter month: 1, it should print January.
# make use of match statement.

num = int(input("Enter Month number:"))
match num:
    case num if num == 1:
        print("You are in January.")
    case _:
        print("Its homework...")

# Write a program to display the quarter of the month.
# Accept Input as month name, i.e. January.

month_num = int(input("Enter Month you are in (1-12): "))

# Match case with if conditional statement.

match month_num:
    case month_num if month_num >=1 and month_num <=3:
        print("You are in fist quarter.")
    case month_num if month_num >= 4 and month_num <= 6:
        print("Second quarter.")

    case _: 
        print("Invalid month.")

# Using logical OR operator (|)

match month_num:
    case 1 | 2 | 3:
        print("You are in first quarter.")
    case 4 | 5 | 6:
        print("You are in second quarter.")
    

# Your program should print, January belongs to 1st Quarter.


