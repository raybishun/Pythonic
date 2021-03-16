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

# Converting decimal to binary