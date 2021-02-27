class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class must implement this!")

# Monkey
class Monkey(Animal):
    def eat(self):
        print("Monkey eating bananas...")

# Bird
class Bird(Animal):
    def eat(self):
        print("Bird eating worms...")
    
    def fly(self):
        print("Bird soaring high above the sky...")


my_monkey = Monkey("Monkey")
my_monkey.eat()

my_bird = Bird("Bird")
my_bird.eat()
my_bird.fly()