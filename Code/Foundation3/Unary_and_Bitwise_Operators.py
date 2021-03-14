# =============================================================================
# Unary Operators (with a single operand)
# =============================================================================
# Bitwise complement operator (the ~), converts to the 'twos complement' of a binary representation
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

# ANDing
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
# Shifting Operators (move either right or left)
# =============================================================================
print("---")
# Right Shift
# -----------------------------------------------------------------------------
a = 0b110           # 6
print(bin(a))
print(bin(a >> 2))  # think of this as pulling digits n to the right, past the decimal and chopping them off
print(a >> 2)
print(a >> 5)       # returns 0 if you attempt to pull more than what's available
print()

# Left Shift
# -----------------------------------------------------------------------------
a = 0b110           # 6
print(bin(a))
print(bin(a << 2))  # think of this as inserting/padding n digits immediately left of the decimal
print(a << 2)       # 24
print()