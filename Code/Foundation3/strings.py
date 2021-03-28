# -----------------------------------------------------------------------------
# Immutability
# -----------------------------------------------------------------------------
greeting = 'hi'
print(f'{id(greeting)}\t{greeting}')

greeting_cap = greeting.capitalize()
print(f'{id(greeting_cap)}\t{greeting_cap}')

greeting2 = greeting
print(f'{id(greeting)}\t{greeting}')
print(f'{id(greeting2)}\t{greeting2}')
print()

# -----------------------------------------------------------------------------
# Parsing str
# -----------------------------------------------------------------------------
greeting = "Hello World"
print(len(greeting))
print(greeting[0])

# Get the last char
print(greeting[len(greeting) -1])
print(greeting[-1]) # d
print()

# -----------------------------------------------------------------------------
# Slicing
# -----------------------------------------------------------------------------
first_four = greeting[0:4]
print(first_four)                   # Hell

print(greeting[:])                  # Hello World
print(greeting[6:])                 # World
print(greeting[6:len(greeting)])    # World
print(greeting[6:11])               # World (NOTE: 1 past the end)

# Step
nums = "0123456789"
print(nums[0:7:1])                  # 123456
print(nums[0:7:2])                  # 0246
print(nums[5:10])                   # 56789 (NOTE: 1 past the end)
print(nums[::-1])                   # 9876543210
print()

# -----------------------------------------------------------------------------
# String Encoding and Functions
# -----------------------------------------------------------------------------
# Encoding formats: Unicode and ASCII
# Unicode: https://en.wikipedia.org/wiki/List_of_Unicode_characters
# strings are Unicode by default (UTF-8 encoded)
# UTF-8 (8 bits are used for storage)
print(ord('a')) # 97

# Print the TM symbol
print('\u2122')
print(chr(8482))
print(chr(0x2122))

