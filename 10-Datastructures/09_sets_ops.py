# Set operations.

sub_1 = {"Maths", "English", "Social"}
sub_2 = {"GeneralKnowledge", "EVS", "English"}
print(f"Original sub_1: {sub_1}")
print(f"Original sub_2: {sub_2}")
# intersection.
sub_intersection = sub_1.intersection(sub_2)
print(f"Intersection: {sub_intersection}")

sub1_difference = sub_1.difference(sub_2)
print(f"Difference: {sub1_difference}")

sub2_difference = sub_2.difference(sub_1)
print(f"Difference in Sub2 compare to sub1: {sub2_difference}")

num1 = {1, 2, 3, 4, 5}
num2 = {1, 2, 3, 4, 5, 6, 7}
is_subset = num1.issubset(num2)
print(f"is num1 subset of num2: {is_subset}")


even_nums = {2, 4, 6, 8}
odd_nums = {3, 5, 7, 9}
is_disjoint = even_nums.isdisjoint(odd_nums)
print(f"Is even_nums disjoint of odd_nums: {is_disjoint}")

# Mathematical logic.
print(" **** Mathmatical logics on Set ****")
print(sub_1 | sub_2) # combines all elements from sets.

print(sub_1 & sub_2) # returns common from both the list.

print(sub_1 - sub_2) # returns elements from sub_1 not present in sub_2.


# Print event and odd numbers using sets.
 # - declare a set with numbers and iterate using for loop, 
 # find even and odd.
# Print revers order of the set.
 # - Declare a set with random elements, print in reverse.
# Print squres of the set using for loop.
