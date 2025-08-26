# Base class
class Vehicle:
    def move(self):
        pass  # To be overridden


class Car(Vehicle):
    def move(self):
        print(f"Driving")


class Plane(Vehicle):
    def move(self):
        print(f"Flying")


class Boat(Vehicle):
    def move(self):
        print(f"Sailing")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
