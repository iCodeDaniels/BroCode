class Car:

    def turn_on(self):
        print("The car is being turned on")
        return self

    def drive(self):
        print("The car is driving")
        return self

    def brake(self):
        print("The brake is activated")
        return self

    def turn_off(self):
        print("You turn off the engine")

Car = Car()
(Car.turn_on()
    .drive()
    .brake()
    .turn_off())