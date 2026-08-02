# List slicing.

numbers = [1, 2, 3, 4, 5, 6, 7]

# slice first 3 elements.
slice_3_ele = numbers[:3] # 3 is exclusive.
print(f"List after slice: {slice_3_ele}")

slice_last_4_ele = numbers[3:] # 3 is inclusive
print(f"Slice last 4 elements: {slice_last_4_ele}")

slice_alternate_ele = numbers[0:7:2]
print(f"Alternate ele slice: {slice_alternate_ele}")
