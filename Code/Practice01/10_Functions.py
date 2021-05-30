# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# Basics
# -----------------------------------------------------------------------------
def greeting(name):
    print(f'Hello {name}!')

# Functions can be passed as an argument
print(greeting)

# Call Function
greeting('Ray')
print()

# Returning Data
# -----------------------------------------------------------------------------
def add_two(num1, num2):
    return num1 + num2

result = add_two(5,3)
print(result)
print()

# Parameters and Arguments
# -----------------------------------------------------------------------------
def contact_card(name, age, car_model):
    return f'{name} is {age}, and drives an {car_model}.\n'

# Passing args based on their 'position'
print(contact_card('Ray', 150, 'E450 Coupe'))

# Passing args based on 'keyword'
print(contact_card(age=150, car_model='E450 Coupe', name='Ray'))

# Passing hybrid of positional and keyword agrs
# NOTE: Once you start using keywords, you can no longer mix args
print(contact_card('Ray', car_model='E450 Coupe', age=150))

# Default args
# NOTE: Default args can only be followed by other default args in the signature
# -----------------------------------------------------------------------------
def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(17))
print(can_drive(17, 21))
print()