"""
- This is a multiline (expensive) string, 
    NOT a block comment
"""

'''
- This is a multiline (expensive) string, NOT a block comment
- Python is a dynamically-typed language, NOT statically-typed
'''

# A comment...

var1 = "hello"
var1 += " world"
print(var1)
print(id(var1))
print(type(var1))

print(var1.find('o'))
print("\"hi\"") # must esc when using "" within ""

print(True > False)
print()

# Numbers (int, float, scientific notation)
x = 2e2             # 200.0
y = 2 * (10 ** 2)   # 200
z = 2e2-2           # 198.0
print(x)
print(y)
print(z)
print(x == y)       # True
print()

# Operators
"""
    / is used for standard division, and ALWAYS returns a float
    // is 'floor division', that is, only the whole number is returned
    % modulus, returns the remainder (a common use of this is to find even/odd numbers)
    ** are exponents 2 ** 3 = (2 x 2 x 2) = 8
"""

# Number Systems
"""
    Base2       Binary          0-1
    Base8       Octal           0-7
    Base10      Decimal         0-9
    Base16      Hexadecimal     0-9, A-F
"""

print(f'Binary:     \t{bin(0b1001)}')
print(f'Octal:      \t{oct(0o11)}')
print(f'Decimal:    \t{0b1001}')
print(f'Hexadecimal:\t{0x9}')
print()

# Converting decimal to binary
'''
...128 64  32  16  8   4   2   1
'''

# Floating-Point Accuracy
"""
- Floats are stored as binary fractions in memory
- However, not all decimals can be represented as binary fractions cleanly, i.e. 0.1
- As a result of this, the computer makes an approximation
"""

# Typecasting
print(float(1))             # 1.0
print(int(1.618))           # Truncates, does not round
print(type(str(1.618)))     # <class 'str'>
print(type(float("1.618"))) # <class 'float'>       
# print(int("1.618"))         # ValueError: invalid literal for int() with base 10: '1.618' (unfortunately, does not truncate)
print(bool(1))              # True; Almost everything in Python has a boolean representation (except for something that evaluates to 0 or none)
print(bool(1.618))          # True
print(bool('hi'))           # True
print(bool(0.00))           # False
print(bool(''))             # False
print('---')
# Checks if left most value is true, then checks the next value
# REMEMBER 'and' requires all tokens to be true
# 'and' will return the first 'falsy' value, or the last 'truthy' value 
print(1 and 0)              # 0 
print(bool(1 and 0))        # False

print(1 and 2)              # 2 
print(bool(1 and 2))        # True

print(1 and 'a')            # a 
print(f"{bool(1)}\t{bool('a')}")    # True, True
print(bool(1 and 'a'))      # True
print('---')

print('a' and 0 and 'b')    # 0 
print(bool('a' and 0 and 'b')) # False

print("---")
print(0 and 1)              # 0
print(1 or 0)               # 1
print(0 or 1)               # 1
print(0 or "")              # return nothing, don't know why??
print(0 or 1 or 'apple')    # 1

print(not 1)                # False
