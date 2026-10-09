from abc import ABC, abstractmethod

class Vehicle(ABC):
    def display(self, name):
        print("Model:", name)

    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is running.")

my_car = Car()
my_car.display("Sedan")
my_car.start()

class Scooter:
    def check(self):
        print("Scooter battery OK.")

print("\n--- Status ---")
Scooter().check()
