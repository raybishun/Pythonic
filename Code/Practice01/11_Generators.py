# =============================================================================
# Generators
# =============================================================================
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

generator = gen_range(10)
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print()

# Calling our gen_range()
# -----------------------------------------------------------------------------
for num in gen_range(10, step=2):
    print(num)          # 1 3 5 7 9
print()

# Convering Generators to Lists
# -----------------------------------------------------------------------------
my_list = list(gen_range(10))
print(my_list)          # [1,2,3...10]
print()

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

my_fib = gen_fib()
print(next(my_fib))     # 1
print(next(my_fib))     # 1
print(next(my_fib))     # 2
print(next(my_fib))     # 3
print(next(my_fib))     # 5
print()

# An alternative to Recursion; here we ask for what the 50th fib
# Recursion would take forever, and likely time out
print([next(my_fib) for _ in range(50)][-1])
print()