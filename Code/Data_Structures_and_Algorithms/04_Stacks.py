class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) < 1:
            print("Stack is empty.")
        else:
            self.stack.pop()

    def print_stack(self):
        print(self.stack)

# Consumer
my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

my_stack.print_stack()