# Functions
# =============================================================================
help(print)

def greeting(name = "John Doe"):
    print(f'Hello, {name}!')
    return 0

def remainder(num1, num2):
    return num1 % num2

# Client
# =============================================================================
print(greeting("Ray"))
greeting()

print(remainder(10, 3))