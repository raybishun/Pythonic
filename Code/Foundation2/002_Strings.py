# =============================================================================
# Strings
# =============================================================================

# Strings are immutable

message = "i'm on mY way.\nwhere aRe you 618?"
print(message)

first_index = message[0]
print(first_index)

last_index = message[-1]
print(last_index)

second_last_index = message[-2]
print(second_last_index)

third_last_index = message[-3]
print(third_last_index)

first_3_char = message[0:3]
print(first_3_char)

get_the_word_my = message[7:9] # start count at 0, then go 1 past what you want returned
print(get_the_word_my)

numbers = '123456789'
print(numbers[0:6:2]) # returns 135 (skips every other value)

print(numbers[5:]) # returns 6789

print(numbers[-2:]) # returns 89

# Common String Methods
# =============================================================================
print(message.upper())
print(message.capitalize()) # capitalize the first char, and lowercase all others
print(message.isdigit())

alpha_numeric = "ABC123"
print(alpha_numeric.isalnum()) # must only have letters and numbers (no spaces or special chars)

print(message.startswith("i'm"))

print(message.startswith("on", 4))

# String Formatting
# =============================================================================
phrase = "Today is {0}, and {0} is the start of the week.".format("Sunday")
print(phrase)

# =============================================================================
# Exercises
# =============================================================================
# Modulo (the remainder...)
remainder = 15 % 4
print(remainder) # return 3
print()
# -----------------------------------------------------------------------------
chars = "[[]]"
word = "Cool"
# chars = "[[{0}]]".format("Cool")
print(chars)

# or
print(f'{chars[:2]}{word}{chars[2:]}')
print()
# -----------------------------------------------------------------------------
word1 = "Tonka"
word2 = "Truck"
# result: "onkaTuck"
print(f'{word1[1:]}{word2[0:1]}{word2[2:]}')
print()
# -----------------------------------------------------------------------------
chars = "<<[]]]"
word = "Cool"

size = len(chars)
print(size)

idx = int(size/2)
print(idx)
print(type(idx))

# result: "<<[Cool]]]"
print(f'{chars[:idx]}{word}{chars[idx:]}')
print()