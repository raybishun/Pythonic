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

