base = float(input("Enter the base number: "))

exponent = int(input("Enter the exponent (a non-negative integer): "))

result = base

for _ in range(1, exponent):
    result *= base

print(f"{base} raised to the power of {exponent} is: {result}")
