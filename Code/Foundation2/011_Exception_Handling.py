def sum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1 + num2)
    else:
        print("invalid data type")
    
first_number = input("Enter first number: ")

try: 
    sum(first_number, 1)
except:
    print("Error")
    print(type(first_number))
