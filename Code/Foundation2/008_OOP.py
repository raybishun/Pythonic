# OOP
# =============================================================================
class Vehicle:
    def __init__(self, make, model):
        self.vehicle_make = make
        self.vehicle_model = model

car1 = Vehicle('MB', 'E450')
print(f'{car1.vehicle_make}\t{car1.vehicle_model}')

car2 = Vehicle('BMW', '5 Series')
print(f'{car2.vehicle_make}\t{car2.vehicle_model}')