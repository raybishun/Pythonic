# -----------------------------------------------------------------------------
# Convert Celsius to Fahrenheit
# -----------------------------------------------------------------------------
celsius = int(input("Enter celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f'{celsius} Celsius is {fahrenheit} Fahrenheit.')

# -----------------------------------------------------------------------------
# Syntax Analysis (the parsing phase) 
# will construct a parse tree using tokens the lexer provided
# -----------------------------------------------------------------------------
"""
(ID)fahrenheit,(EQUALS)=,(RPAREN)(,(ID)celsius,(TIMES)*,(NUM)9,(DIV)/,(NUM)5,(LPAREN)),(PLUS)+,(NUM)32
"""

# TODO: Draw as a tree