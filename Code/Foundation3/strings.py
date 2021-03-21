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