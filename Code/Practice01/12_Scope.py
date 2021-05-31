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

while y < 6: # Exception: 'y is not defined '
    print(y) 
    y += 1   

print(y)     
print()