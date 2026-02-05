print("Enter key-value pairs as 'key=value', one pair per line. Enter 'done' to finish.")
kwargs = {}
while True:
    entry = input("Enter key-value pair: ")
    if entry.lower() == 'done':
        break
    if '=' in entry:
        key, value = entry.split('=', 1)
        kwargs[key.strip()] = value.strip()
    else:
        print("Invalid input format. Please use 'key=value' format.")

print("\nCollected key-value pairs:")
for key, value in kwargs.items():
    print(f"{key}: {value}")
    