# Unary Operators
# -----------------------------------------------------------------------------
# Bitwise complement operator (the ~), converts to the 'twos complement' of a binary representation
# Twos complement is a way of representing a negative number
# Shortcut is:  complement  a = -1 * a - 1
a = 0b010
print(a)        # a = 2
print(bin(a))   # 0b10
print(~a)       # -3 (-1 * a - 1)


# Truth Tables
# -----------------------------------------------------------------------------
a = 0b1001      # 9
print(a)