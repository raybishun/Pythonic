"""
- This is a multi-line string object!!!
- Not a comment block!!!
"""

'''
- This is also a multi-line string object!!!
- Not a comment block!!!
'''

# Use of single quotes ('...') with a string literal
greeting1 = 'Hello, World!'

# Use of double quotes ("...") with a string literal
greeting2 = "Hello, World!"

# Python is not strongly typed
greeting1 = 1.618

print(greeting1)
print(greeting2)

print(greeting1)

index = greeting2.find(',')
print(index)

# Scientific Notation
scientific_notation = 4.5e9
x = 4.5 * (10 ** 9)
print(scientific_notation == x)

# Normal Division
print( 5 / 3 )

# Floor Division
# Return the number of times 5 'evenly' divides into 3s, as an int
print ( 5 // 3 ) 

# Modulo
# Return the remainder as an int
# Common usage for modulo is to identify odd or even numbers
print ( 5 % 3 )

# Exponents
print ( 2 ** 3 ) # 2 x 2 x 2

# Number Systems
# -----------------------------------------------------------------------------
# Decimal       is  Base 10     0 - 9
# Binary        is  Base 2      0 or 1
# Octal         is  Base 8      0 - 7
# Hexadecimal   is  Base 16     0 - F (0 - 9 and A - F)

# Representing Number Systems
# -----------------------------------------------------------------------------

# Prefix: 0b for Binary
print(0b101)

# Prefix: 0o for Octal
print(0o7242)

# Prefix: 0x for Hexadecimal
print(0xFF012)

# Converting Decimal to Binary
# -----------------------------------------------------------------------------
# Divide the Decimal by the number system's base that we want to covert to, i.e.
myDecimal_Number = 15
myBase = 2

result1 = myDecimal_Number % myBase
print(f'result1: {result1}') # remainder is 1

result2 = result1 % myBase
print(f'result2: {result2}')  # remainder is 1

result3 = result2 % myBase
print(f'result3: {result3}')  # remainder is 1

result4 = result3 % myBase
print(f'result4: {result4}')  # remainder is 1

# The remainders from Least Significant to Most Significant
print(f'{result1}{result2}{result3}{result4}') # returns 1111


# Converting from Binary, back to Decimal (where the binary value is 1111)
# -----------------------------------------------------------------------------
# Most Significant .......... Least Significant
#  (1 * 2^3)  +  (1 * 2^2) + (1 * 2^1) + (1 * 2^0)   where ^ is 'power'
# (1 * 2*2*2) +  (1 * 2*2) + (1 * 2) + (1)
#        8    +        4   +      2  +  1 = 15

# Issue with Floating-Point Accuracy
# -----------------------------------------------------------------------------
# In memory, Floating-Point numbers are stored as binary fractions
# However, not all decimals can be represented as binary fractions, i.e. 0.1
# So a rounding approximation is made