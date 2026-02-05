items_dict = {}

print("Enter key-value pairs for the dictionary (key:value), one pair per line. Enter 'done' to finish.")

while True:

    entry = input("Enter key-value pair (key:value): ")

    if entry.lower() == 'done':
        break

    key, value = entry.split(':')
    items_dict[key.strip()] = value.strip()

size_of_dict = len(items_dict)

print("The size of the dictionary is:", size_of_dict)