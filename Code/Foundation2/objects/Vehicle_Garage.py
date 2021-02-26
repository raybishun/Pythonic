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

    def drive(self):
        print("Vehicle driving...")

class Truck(Vehicle):
    def drive(self):
        print("Truck driving...")

class Motorcycle(Vehicle):
    def drive(self):
        print("Motorcycle riding...")