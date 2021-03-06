my_file = open('Z:\Git\Pythonic\Code\Foundation2\sample.txt')

# Read file
# -----------------------------------------------------------------------------
first_read_attempt = my_file.read()
print(first_read_attempt)

second_read_attempt = my_file.read()
print(second_read_attempt)

# Reset the cursor
my_file.seek(0)

third_read_attempt = my_file.read()
print(third_read_attempt)

# Convert file to a list (each line is converted to an element in the list)
# -----------------------------------------------------------------------------
# Reset the cursor
my_file.seek(0)

my_file_tolist = my_file.readlines()
print(my_file_tolist)

my_file.close()


# 'with open' (NOTE: The file is automatically closed !!!)
# -----------------------------------------------------------------------------
print("---------------")
# Append
with open('Z:\Git\Pythonic\Code\Foundation2\sample.txt', mode='a') as my_file2:
    my_file2.write("\nMy new line...")
    
with open('Z:\Git\Pythonic\Code\Foundation2\sample.txt', mode='r') as my_file2:
    print(my_file2)

with open('Z:\Git\Pythonic\Code\Foundation2\sample.txt', mode='w') as my_file2:
    my_file2.write("\nWhen mode is set to 'w', the file is overwritten...")
    print(my_file2)

with open('Z:\Git\Pythonic\Code\Foundation2\sample2.txt', mode='r+') as my_file2:
    my_file2.write("\nr+ means, open file for both reading and writing...")
    my_file2.read()
    print(my_file2)

with open('Z:\Git\Pythonic\Code\Foundation2\sample2.txt', mode='w+') as my_file2:
    my_file2.write("\nw+ means, overwrite and write...")
    my_file2.read()
    print(my_file2)