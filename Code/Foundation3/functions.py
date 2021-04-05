# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def greeting(str):
    print(f'Hello, {str}')

def greeting2(name):
    print(f'Hello, {name}')

def add(num1, num2):
    return num1 + num2

# One or more default args MUST be the LAST args in the def signature
def user_info(name, email, location='WA'):
    return f'\"{name}\",\"{email}\",\"{location}\"'

# -----------------------------------------------------------------------------
# Consume Functions
# -----------------------------------------------------------------------------
greeting('Ray')
greeting(1.618)
print(add(5, 3))

# Passing args by position (positional args)
print(user_info("Ray", 'ray@mail.com'))

# Passign args by keyword
print(user_info(location='NY', name="Ray", email='ray@mail.com', ))

# Mix (*** NOTE, once use start uing keyword args, you MUST pass all
# args using keyboard, you CANNOT switch back to using positional args)
print(user_info("Ray", location='FL', email='ray@mail.com', ))