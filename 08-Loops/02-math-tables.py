# Table 1.
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# ...
# 1 * 20 = 20

print("*" * 5 + " 1st Table " + "*" * 5)

table_of = 3
for num in range(1, 21):
    mul_val = table_of * num
    print(f"{table_of} * {num} = {mul_val}")

