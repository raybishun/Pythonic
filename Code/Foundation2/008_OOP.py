# OOP
# =============================================================================
class Vehicle:
    # Class variables (should NOT be changed, similar to static in C#)
    vehicle_count = 0
    dealership = 'Pargon Motors'

    def __init__(self, make, model):
        # Instance variables
        Vehicle.vehicle_count += 1
        self.vehicle_make = make
        self.vehicle_model = model
    
    def get_vehicle_count(self):
        return Vehicle.vehicle_count

    def get_model(self, str):
        return f'{str}, you have a brand new: {self.vehicle_model}!!!'


car1 = Vehicle('MB', 'E450')
print(f'{car1.vehicle_make}\t{car1.vehicle_model}')

car2 = Vehicle('BMW', '5 Series')
print(f'{car2.vehicle_make}\t{car2.vehicle_model}')

print(car1.dealership)
print(car2.dealership)

print(car1.get_vehicle_count())
print(car2.get_vehicle_count())
print(Vehicle.vehicle_count)

print(car1.get_model("Ray"))