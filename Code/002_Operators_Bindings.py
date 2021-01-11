# Operators and Bindings


# Get int from binary 
a = 0b010
print(a) # returns 2

# Get binary fron int
print(bin(a)) # returns 0b10

# Bitwise Complement operator 
# Converts over to Two's complement of our binary representation
# Two's complement is a way to represent negative numbers, and always begins with a 1
print (~a) # retuns -3

# The formula is: your_number * -1 subtract 1
print(a * -1 - 1)

print(bin(~a)) # returns -0b11