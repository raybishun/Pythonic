if 'a' < 'b':
    print(ord('a'))
else:
    print('else...')

print(f"Value of b is: {ord('b')}")
print()

# if/else
if False:
    print("is false")
else:
    print("is true")
print()

if True:
    print("is true")
else:
    print("is flase")
print()

# elif
today = "Wed"
if today is "Mon":
    print("Mon")
elif today is "Tue":
    print("Tue")
elif today is "Wed":
    print("Wed")
print()


play = input("Shall we play a game? ")
if len(play) > 0:
    if play == 'y':
        print('great!!!')
    elif play == 'n':
        print('you da stupid...')
elif len(play) <= 0:
    print("Invalid input...")

# pass
if True:
    print("pass is a 'no-o'")
    pass
