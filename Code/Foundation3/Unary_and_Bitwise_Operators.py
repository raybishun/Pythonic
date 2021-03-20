# =============================================================================
# Unary Operators (one with only a single operand)
# =============================================================================
# Bitwise complement operator, the ~ converts to the 'twos complement' of a binary representation
# Twos complement is a way of representing a negative number
# Shortcut is:  complement  a = -1 * a - 1
a = 0b010
print(a)            # a = 2
print(bin(a))       # 0b10
print(~a)           # -3 (-1 * a - 1)
print()

# =============================================================================
# Truth Tables [OR, AND, XOR (exclusive OR), NOT]
# =============================================================================

# ORing
# -----------------------------------------------------------------------------
a = 0b1001          # 9
b = 0b1100          # 12
print(bin(a))
print(bin(b))
print(bin(a | b))
#   0b1101
print()

# ANDing (both must be 1, to return 1)
# -----------------------------------------------------------------------------
a = 0b1001          # 9
b = 0b1100          # 12
print(bin(a))
print(bin(b))
print(bin(a & b))
#   0b1000
print()

# XORing (exclusive OR), that is, only 1 can be true, to return true
# -----------------------------------------------------------------------------
a = 0b1001          # 9
b = 0b1100          # 12
print(bin(a))
print(bin(b))
print(bin(a ^ b))
#   0b101
print()

# =============================================================================
# Shif Operators (move either right or left)
# =============================================================================
print("--- Shift Operators ---")
# Right Shift
# -----------------------------------------------------------------------------
a = 0b110           # 6
print(bin(a))       # 0b110
print(bin(a >> 2))  # 0b1   (think of this as pulling digits n to the right, past the decimal and chopping them off)
print(a >> 2)       # 1
print(a >> 5)       # 0     (0 if returned if you attempt to pull more than what's available)
print()

# Left Shift
# -----------------------------------------------------------------------------
a = 0b110           # 6
print(bin(a))       # 0b110
print(bin(a << 2))  # 0b11000 (think of this as inserting/padding n digits immediately left of the decimal)
print(a << 2)       # 24
print()

# =============================================================================
# Boolean Operators
# =============================================================================
# not
print(not True)         # False ('not' is a unary operator)
print()

# or
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
print()

# and (BOTH must be true to return true)
print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False
print()

# =============================================================================
# Comparison Operators
# =============================================================================
'''
<
>
<=
>=
==
!=      
is (the identity operator; tests if the same OBJECT)
is not
'''
print(a > b)
print(f'{ord("a")}, {ord("b")}')
print(f"{ord('a')}, {ord('A')}")
print(f"{id('a')}, {id('A')}") # where in memory
print()

print([] is []) # actually returns False (because lists are mutable)
print([] == [])
print()

# =============================================================================
# Operator Priority
# =============================================================================
"""
Parenthesis and List/Dictionary/Set literals
Accessing attributes (subscription, slicing, function/method call, attribute reference)
Exponentiation (**)
Positive, Negative, and bitwise complement
Multiplication *, Division /, Floor Division //, Modulo %
Addition +, Subtraction -
Bitwise Shifts << & >>
Bitwise AND &
Bitwise XOR ^
Bitwise OR |
Comparison operators (in, not in, is, is not, <, >, <=, >=, ==, !=)
Boolean NOT not
Boolean AND and
Boolean OR or
Conditions if
"""