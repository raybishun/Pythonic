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