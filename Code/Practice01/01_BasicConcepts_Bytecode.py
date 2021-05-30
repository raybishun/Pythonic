# -----------------------------------------------------------------------------
# Show the bytecode of a function
# -----------------------------------------------------------------------------
import dis

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(convert_celsius_to_fahrenheit(10))
print()

# Display the disassembled bytecode of the function.
dis.dis(convert_celsius_to_fahrenheit)