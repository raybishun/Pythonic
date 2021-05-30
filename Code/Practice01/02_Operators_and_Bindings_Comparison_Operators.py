# =============================================================================
# Operators and Bindings: Comparison Operators
# =============================================================================

# -----------------------------------------------------------------------------
# Testing with immutables
# -----------------------------------------------------------------------------
print(1 < 2)
print(1 <= 2)
print('a' < 'b')
print()

print(f'{ord("a")}\t{ord("b")}')
print(f'{ord("A")}\t{ord("B")}')
print()

print('a' == 'A')
print()

print( 1 == 1.0 )   # True
print(1 is 1.0)     # False
print(1 is not 1.0) # True
print(id(1))
print(id(1.0))
print()

print(type(1))
print(type(1.0))

print(1 != 2)
print()

a = "Hello"
b = "Hello"
print(a is b)   # True
print(id(a))
print(id(b))
print()

# -----------------------------------------------------------------------------
# Testing with mutables, i.e. lists
# -----------------------------------------------------------------------------
print([] is []) # False
print()