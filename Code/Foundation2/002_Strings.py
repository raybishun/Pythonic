# =============================================================================
# Strings
# =============================================================================
message = "I'm on my way.\nWhere are you?"
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
