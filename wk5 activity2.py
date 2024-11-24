class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Example usage
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
