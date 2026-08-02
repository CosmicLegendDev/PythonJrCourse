#4. Write a program to print below pattern, using loop and range()
#      *
#     * *
#    * * *
#   * * * * 
n = 6
for i in range(1, n):
     print(" " * (n - i), end=" ")
     print("* " * i)


# n=6
# l1: i = 1 , n-i = 5
#      *
# l2: i = 2, n-i = 4
#     * *
# l3: i = 3, n-i = 3
#    * * *