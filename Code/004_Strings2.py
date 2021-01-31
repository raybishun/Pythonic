# Unicode code points
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('\u2122')) # The TM symbol

# Convert back to a string
print(chr(8482)) # The TM symbol

# A few String Methods...
hello = 'HeLlo WoRlD'
print(hello.lower())
print(hello.upper())
print(hello.capitalize())
print(hello.title())

print(hello.isascii())
print(hello.islower())

print()

some_str_as_a_num = "10.0"
print(some_str_as_a_num.isdecimal()) # returns false (because of the decimal???)

some_str_as_a_num2 = "10"
print(some_str_as_a_num2.isdecimal()) # returns true

some_str_as_a_num = "10.0"
print(some_str_as_a_num.isnumeric()) # here too returns false (because of the decimal???)

some_str_as_a_num2 = "10"
print(some_str_as_a_num2.isnumeric()) # returns true

print()

some_str_as_a_num = "10.0"
print(some_str_as_a_num.isalpha()) # returns false

some_str_as_a_num = "ten"
print(some_str_as_a_num.isalpha()) # returns true

print()

possible_var_or_function_name = "1test"
print(possible_var_or_function_name.isidentifier()) # returns false

some_output = "print me please\n"
print(some_output.isprintable()) # returns false due to the ESC character
