multi_dict = {}

print("Enter key followed by its values (separated by spaces). Enter 'done' to finish.")

while True:

    entry = input("Enter key and values (key value1 value2 ...): ")

    if entry.lower() == 'done':
        break
    
    inputs = entry.split()
    key = inputs[0]
    values = inputs[1:]

    if key in multi_dict:
        multi_dict[key].extend(values)

    else:
        multi_dict[key] = values

print("Dictionary with keys having multiple inputs:")

for key in multi_dict:
    print(f"{key}: {multi_dict[key]}")