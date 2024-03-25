from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):

    def go(self):
        print("You can drive the car")

    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You can ride the motorcycle")

    def stop(self):
        print("The motorcycle has come to a stop")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()