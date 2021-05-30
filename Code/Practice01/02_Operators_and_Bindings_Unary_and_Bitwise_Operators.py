# =============================================================================
# # Operators and Bindings: Unary and Bitwise Operators
# =============================================================================

# -----------------------------------------------------------------------------
# Unary Operators (a single operand)
# -----------------------------------------------------------------------------
# I.e., the Bitwise Complement Operator: ~
# AKA, the twos compliment operator (is a way of expressing a negative number)
# (Simple formula: make negative, and subtract 1)
print(~1)   # -2
print(~2)   # -3
print(~3)   # -4
print(~10)  # -11
print()

# -----------------------------------------------------------------------------
# Bitwise Operators (truth tables)
# -----------------------------------------------------------------------------
# Comprised of: OR, AND, XOR (Exclusive OR)
a = 0b1001
b = 0b1100
print(bin(a))
print(bin(b))

# OR (either must be true to set as 1)
print(bin(a | b))
print()

# a     0b1001
# b     0b1100
# OR    0b1101

# AND (both must be true to set as 1)
print(bin(a))
print(bin(b))
print(bin(a & b))
print()

# a     0b1001
# b     0b1100
# AND   0b1000

# XOR (aka, Exclusive OR, ONLY one must be true to set as 1)
print(bin(a))
print(bin(b))
print(bin(a ^ b))
print()

# a     0b1001
# b     0b1100
# OR    0b0101

# -----------------------------------------------------------------------------
# Shift Operators (move binary digits to the left or right)
# -----------------------------------------------------------------------------
a = 0b110

# Right-Shift
'''
Imagine an end of line marker, and pull the digits past the end, then truncate
'''
print(bin(a >> 2))  # 0b1
print(bin(a >> 10)) # simply returns 0b0, when you went pull past the digits that are provided
print()

# Left-Shift
'''
Imagine an end of line marker, and you're padding 0s to the immediate left of the end
'''
print(bin(a << 2))  # 0b11000
print()