class Animal:
    def __init__(self):
        print("Animal ctor...")
    def move(self):
        print("Animal moving...")
    def eat(self):
        print("Animal eating...")

class Bird(Animal):
    def __init__(self, age, name):
        # Animal.__init__(self)
        self.age = age
        self.name = name
    def move(self):
        print("Bird flying...")

class Fish(Animal):
    def __init__(self, age, name):
        # Animal.__init__(self)
        self.age = age
        self.name = name
    def move(self):
        print("Fish swimming...")

class Dog(Animal):
    def __init__(self, age, name):
        # Animal.__init__(self)
        self.age = age
        self.name = name
    def move(self):
        print("Dog running...")


my_dog = Dog(5, "Sparky")
my_dog.move()
my_dog.eat()

my_fish = Fish(1, "Nemo")
my_fish.move()
my_fish.eat()

my_bird = Bird(5, "Crazy")
my_bird.move()
my_bird.eat()