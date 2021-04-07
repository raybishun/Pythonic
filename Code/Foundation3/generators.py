# -----------------------------------------------------------------------------
# Generators
# -----------------------------------------------------------------------------

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num # 'yield' returns then pauses...
        num += step

# -----------------------------------------------------------------------------
# Manual Looping
# -----------------------------------------------------------------------------
print(gen_range)            # returns the mem address of the generator
print()

my_generator = gen_range(3)
print(next(my_generator))   # 1
print(next(my_generator))   # 2
print(next(my_generator))   # 3
print()

# -----------------------------------------------------------------------------
# Automated Looping
# -----------------------------------------------------------------------------
# Return odd numbers in a range of 10, by using a 2 step :)
# Unlike the 'Manual Looping' exaple above, 'for' automatically calls 'next'
for i in gen_range(10, step=2):
    print(i)

print()

# -----------------------------------------------------------------------------
# Convert Generator to List
# -----------------------------------------------------------------------------
my_generator = gen_range(5)
print(list(my_generator))
print()

# -----------------------------------------------------------------------------
# Infinite Generator 
# -----------------------------------------------------------------------------
def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

get_fib = generate_fibs()
print(next(get_fib))   # 1
print(next(get_fib))   # 1
print(next(get_fib))   # 2
print(next(get_fib))   # 3
print(next(get_fib))   # 5
print(next(get_fib))   # 8
print(next(get_fib))   # 13
print(next(get_fib))   # 21
# ...
print()

# DANGEROUS
# print(list(get_fib))    # Will eventually return 'Killed'

# -----------------------------------------------------------------------------
# Generator are so much faster than recursion
# -----------------------------------------------------------------------------
get_fib = generate_fibs()
print([next(get_fib) for _ in range(15)][-1])
print([next(get_fib) for _ in range(150)][-1])