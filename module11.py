print("Enter key-value pairs for the dictionary (key:value), one pair per line. Enter 'done' to finish.")
data = {}

while True:

    entry = input("Enter key-value pair (key:value): ")
    if entry.lower() == 'done':
        break

    key, value = entry.split(':')
    data[key.strip()] = value.strip()

sorted_dict_by_key = dict(sorted(data.items()))

print("Sorted dictionary by keys:")

for key in sorted_dict_by_key:
    print(f"{key}: {sorted_dict_by_key[key]}")