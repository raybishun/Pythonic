# -----------------------------------------------------------------------------
# Global Scope
# -----------------------------------------------------------------------------
if 1 < 2:
    x = 3

while x < 4:
    print(x)    # 3
    x += 1

print(x)        # 4

# -----------------------------------------------------------------------------
# Local Scope
# -----------------------------------------------------------------------------
def my_function():
    y = 3

# while y < 4:    # Exception: name 'y' is not defined
#     print(y)
#     y += 1

# print(y)
print()

# -----------------------------------------------------------------------------
# Variable Name Hiding (aka Shadowing)...but I don't know why?? same as above...
# -----------------------------------------------------------------------------
y = 5

def my_other_function(y):
    print(f'Function\'s y is: {y}')
    print(id(y))

my_other_function(10)

print(f'Value of of \'global y\' is: {y}')
print(id(y))
print()
print()

# -----------------------------------------------------------------------------
# Global Keyword (creating a global variable inside a function)
# -----------------------------------------------------------------------------
def my_other_function2(n):
    global g
    g = n + 1
    print(f'Value of g in the function is: {g}')
    print(id(y))

my_other_function2(100)

print(f'Value of of g outside of function: {g}')
print(id(y))