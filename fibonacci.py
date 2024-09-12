def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

limit = int(input("Enter the limit for Fibonacci sequence: "))
print(f"Fibonacci sequence up to {limit}: {fibonacci(limit)}")
