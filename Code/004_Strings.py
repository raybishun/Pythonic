# Strings
# -----------------------------------------------------------------------------
myStr = 'my string'
print(f'{myStr}', f'{id(myStr)}')

# this actually creates a NEW string
myStr = myStr.capitalize() 
print(f'{myStr}', f'{id(myStr)}')

print()


# Immutability of Strings
# -----------------------------------------------------------------------------

# Here the 2 variables are pointing to the same memory location

myStr = "Ray"
print(f'{myStr}', f'{id(myStr)}')

myOtherStr = "Ray"
print(f'{myOtherStr}', f'{id(myOtherStr)}')

print()

# .len(string)
# -----------------------------------------------------------------------------
myStr = "Hello World"
print(len(myStr))

print()

# Indexing
# -----------------------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[2])

lastLetter = alphabet[len(alphabet) - 1]
print(lastLetter)
print(alphabet[-1]) # returns z
print(alphabet[-3]) # returns x

print()

# Slicing
# -----------------------------------------------------------------------------
first3 = alphabet[0:3]
print(first3)

last3 = alphabet[23:26]
print(last3)

last3a = alphabet[23:len(alphabet)]
print(last3a)

last3betterChoice = alphabet[23:]
print(last3betterChoice)

numbers = "123456789"
even = numbers[1:9:2]
print(even)

startToFive = numbers[:5:]
print(startToFive)

two = numbers[1::9]
print(two)

three = numbers[2::9]
print(three)

reverseStr = numbers[::-1]
print(reverseStr)

print()