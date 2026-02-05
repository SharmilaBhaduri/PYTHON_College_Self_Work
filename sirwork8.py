#python program of Python Function with No Arguments, and  Return Value .
def calculate_factorial():
    num = 5 
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

result = calculate_factorial()

print("Factorial of 5:", result)