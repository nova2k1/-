class Vehicle:
    def move(self):
        pass
        
        
class Car(Vehicle):
    def move(self):
        print("Ведет машину")
        
        
class Bike(Vehicle):
    def move(self):
        print("Едет на байке")
        
        
class VehicleFactory:
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")
            
            
vehicle_factory = VehicleFactory()
car = vehicle.factory.create.vehicle("car")
car.move()

bike = vehicle.factory.craete.vehicle("bike")
bike.move()