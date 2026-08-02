# You have marks of 1 students in all subjects,
# I want to calculate sum, max, min, avg.

marks_secured = [98, 92, 91, 89, 67]

total_marks = sum(marks_secured)
print(f"Total Marks secured: {total_marks}")

max_marks = max(marks_secured)
print(f"Max marks {max_marks}")

min_marks = min(marks_secured)
print(f"Min marks secured: {min_marks}")

size_of_marks_secured = len(marks_secured)
avg_marks = total_marks/size_of_marks_secured
print(f"Average marks secured: {avg_marks}")