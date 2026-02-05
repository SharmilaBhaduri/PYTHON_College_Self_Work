num = input("Enter numbers separated by spaces: ").split()
num = list(map(int, num))
result = [(n, n ** 3) for n in num]
print("List of tuples (number, cube):", result)