# =============================================================================
# Input and Output: Type Casting
# =============================================================================
"""
Common Types:
- int
- float
- string
- bool
"""

print(float(10))

print(int(1.618)) # turncates, does NOT round

print(str(1))

print(str(1.0))

print(int('1'))

print(int("1"))

# bool (every type as a boolean representation)
print(bool(1))
print(bool(1.1))
print(bool("Hi"))

# Type that returns 0 or null is typically false
print(bool(''))
print(bool(""))
print(bool(0))
print(bool(None))

print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)

print('a' and 0 and 'y') # only the first 2 values are checked
print()

# OR
print(0 or 1)
print(1 or 0)
print()

# NOT
print(not '')
print(not "")
print(not 0)
print(not 1)