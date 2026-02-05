print("Enter multiple arguments separated by spaces:")
user_input = input()

arguments = user_input.split()

print("Printing multiple arguments:")
print(*arguments)