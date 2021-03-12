# =============================================================================
# Unary Operators (with a single operand)
# =============================================================================
# Bitwise complement operator (the ~), converts to the 'twos complement' of a binary representation
# Twos complement is a way of representing a negative number
# Shortcut is:  complement  a = -1 * a - 1
a = 0b010
print(a)        # a = 2
print(bin(a))   # 0b10
print(~a)       # -3 (-1 * a - 1)
print()

# =============================================================================
# Truth Tables [OR, AND, XOR (exclusive OR), NOT]
# =============================================================================

# ORing
# -----------------------------------------------------------------------------
a = 0b1001      # 9
b = 0b1100      # 12
print(bin(a))
print(bin(b))
print(bin(a | b))
print()

# ANDing
# -----------------------------------------------------------------------------
a = 0b1001      # 9
b = 0b1100      # 12
print(bin(a))
print(bin(b))
print(bin(a & b))
print()

# XORing (exclusive OR), that is, only 1 can be true, to return true
# -----------------------------------------------------------------------------
a = 0b1001      # 9
b = 0b1100      # 12
print(bin(a))
print(bin(b))
print(bin(a ^ b))