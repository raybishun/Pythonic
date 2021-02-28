class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Override string method
    def __str__(self):
        return f'{self.name}\t{self.age}'

    # Override len method
    def __len__(self):
        return self.age


# Tests
tom = Employee("Peter Parker", 25)
print(tom)
print(len(tom))
