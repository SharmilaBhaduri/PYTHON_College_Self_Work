from functools import reduce

n = int(input("Enter the value of n: "))

fibonacci_series = reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print("Fibonacci series up to", n, ":", fibonacci_series[:n])
