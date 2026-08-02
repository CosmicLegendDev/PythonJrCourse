sliced_str = "GuhanKanthan"[0:5] # "yourstring"[start:end] - here end is exclusive.
print(sliced_str)

sliced_str2 = "GuhanKanthan"[:5] # no start index, means start from 0
print(sliced_str2)

sliced_str3 = "GuhanKanthan"[5:] # no end index, means till end of the string.
print(sliced_str3)

sliced_str4 = "GuhanKanthan"[:-7] 
print(f"Slice with negative values as end index: {sliced_str4}")

sliced_str5 = "GuhanKanthan"[-10:] 
print(f"Slice with negative values as start index: {sliced_str5}")
