# -----------------------------------------------------------------------------
# Recursion
# -----------------------------------------------------------------------------

# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11,  12,  13,  14,  15,  16,   17...
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597...

def find_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return find_fib(n - 2) + find_fib(n - 1)

fib_sequence = int(input("Get fib value a sequence? "))
print(find_fib(fib_sequence))

# NOTE
# Python doesn't use 'Tail Call Optimization', 
# so the higher the value, the longer it will take to complete