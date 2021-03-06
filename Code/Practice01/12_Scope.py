# =============================================================================
# Scope
# =============================================================================

# NOTE: *** Conditionals and Loops DO NOT define their own scopes
# Meaning, variables are accessible from anywhere
# -----------------------------------------------------------------------------
if 1 < 2:
    x = 5

while x < 6:
    print(x)    # 5
    x += 1      # x is now 6

print(x)        # 6
print('---')

# Functions define their own scope
# Meaning, variables within a function have a local scope
# -----------------------------------------------------------------------------
def set_y():
    y = 5

set_y()

# while y < 6: # Exception: 'y is not defined '
#     print(y) 
#     y += 1   

# print(y)     
print()

# Name Hiding (aka Shadowing)
# -----------------------------------------------------------------------------
y = 5

def set_x(y):               
    print("Inner y: ", y)   # 10
    x = y
    y = x

set_x(10)

print("Outer y: ", y)       # 5
print()

# Global Keyword
# -----------------------------------------------------------------------------
y = 5

def set_x(z):               
    x = z
    global y    # if 'y' not exists outside function, it does now with global scope
    global a    # if 'a' not exists outside function, it does now with global scope
    y = x
    a = 7

print("y before set_x: ", y)
set_x(10)
print("y after set_x: ", y)
print("a after set_x: ", a) # NOTE: You can actually access a OUTSIDE the function because it's global
print()