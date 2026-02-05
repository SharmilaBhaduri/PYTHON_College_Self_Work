items_dict = {}

print("Enter key-value pairs for the dictionary (key:value), one pair per line. Enter 'done' to finish.")

while True:

    entry = input("Enter key-value pair (key:value): ")

    if entry.lower() == 'done':
        break

    key, value = entry.split(':')

    items_dict[key.strip()] = float(value.strip())

total_sum = sum(items_dict.values())

print("The sum of all items in the dictionary is:", total_sum)