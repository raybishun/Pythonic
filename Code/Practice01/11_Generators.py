# =============================================================================
# Generators
# =============================================================================
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

generator = gen_range(10)
print(next(generator))
print(next(generator))
print(next(generator))
print()

# Calling our gen_range()
# -----------------------------------------------------------------------------
for num in gen_range(10, step=2):
    print(num)
print()