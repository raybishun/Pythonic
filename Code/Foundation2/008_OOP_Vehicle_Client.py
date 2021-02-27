from objects.vehicles.Vehicle_Garage import Vehicle, Truck, Motorcycle

truck1 = Truck("Ford", "F150")
car1 = Vehicle("MB", "E500")
moto3 = Motorcycle("Honda", "CBR 750")

for v in [truck1, car1, moto3]:
    v.drive()

def perform_tasks(vehicle_object):
    vehicle_object.drive()