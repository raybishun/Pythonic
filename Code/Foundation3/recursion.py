# -----------------------------------------------------------------------------
# Recursion
# -----------------------------------------------------------------------------

# Fibonacci Sequence

# Sample: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n -1)

get_fib_sequence = int((input("Get fib sequence for: ")))
print(fib(get_fib_sequence)) # 15 returns 610