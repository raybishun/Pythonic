import sys
# -----------------------------------------------------------------------------
# argv
# -----------------------------------------------------------------------------
# print(sys.argv[0]) # prg name
# print(sys.argv[1]) # a
# print(sys.argv[2]) # b
# print(sys.argv[3]) # c

# TEST: python3 014_Cmd_line.args.py a b c 

# -----------------------------------------------------------------------------
# Accept an unlimited number of arguments
# -----------------------------------------------------------------------------
print(sys.argv[1:])

args = sys.argv[1:]

for arg in args:
    print(arg)

# TEST: python3 014_Cmd_line.args.py a b c d e f g