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

# XOR, aka Exclusive Or (only one must be true)
c = bin(a ^ b)
print(bin(a))
print(bin(b))
print(f' {c}')
print()

# Shift Operators (change the binary representation by moving right or left)
# -----------------------------------------------------------------------------
a = 0b110
print(a) # returns 6 (4 + 2)
print()

# Right-Shift
print(a >> 2) # returns 1
print()

print(a >> 4) # NOTE: returns 0 if you shift more than the number you have
print()

# Left-Shift (padds with leading 0s)
print(a << 2) # returns 24
print()

# Boolean Operators (1=true, 0=false), 
#   and of course the 'not', 'or', 'and' operators
# -----------------------------------------------------------------------------
a = True
print(bin(a)) # returns 0b1

print(not False) # returns True

print(True or False) # returns True

print(False or False) # *** actually returns False ***

print(False and False) # *** actually returns False ***

print()

# Comparison Operators
# -----------------------------------------------------------------------------
print(ord('A'))
print(ord('B'))
print(ord('C'))
print()
print(ord('a'))
print(ord('b'))
print(ord('c'))
print()

# Comparing 'Objects'
print (1 is 1.0) # False
print (1 is not 1.0) # True
print()
# Get an Object's ID in memory
print(id('A'))
print(id('a'))
