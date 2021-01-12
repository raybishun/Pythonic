# Operators and Bindings
# -----------------------------------------------------------------------------
# Get int from binary 
a = 0b010
print(a) # returns 2

# Get binary fron int
print(bin(a)) # returns 0b10

# Bitwise Complement operator 
# -----------------------------------------------------------------------------
# Converts to Two's complement of a binary number
# Two's complement is a way to represent negative numbers, 
# and they always begins with a 1
print (~a) # retuns -3

# The formula is: your_number * -1 subtract 1
print(a * -1 - 1) # retuns -3

# Or simply
print(-a -1) # retuns -3

# Binary representation of Complement 'a'
print(bin(~a)) # returns -0b11

# Truth Tables (AND, OR, XOR, NOT)
# -----------------------------------------------------------------------------
print()
a = 0b1001
b = 0b1100

# AND (both must be true)
c = bin(a & b)
print(bin(a))
print(bin(b))
print(c)
print()

# OR (one must be true)
c = bin(a | b)
print(bin(a))
print(bin(b))
print(c)
print()