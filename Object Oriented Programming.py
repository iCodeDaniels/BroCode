# OBJECT IS AN INSTANCE OF A CLASS
from Car import Car

car1 = Car("Chevrolet", "Corvette", 2023, "White")
car2 = Car("Ford", "Mustang", 2023, "Black")
car3 = Car("Mercedez", "Brabus", 2024, "White")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)

print(car3.make)
print(car3.model)
print(car3.year)
print(car3.color)

car1.drive()
car2.drive()
car3.drive()