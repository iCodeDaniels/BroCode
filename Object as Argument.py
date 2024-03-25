class Car:

    color = None

def change_color(car,color):

    car.color = color
class Bicycle:

    color = None
def change_color(bicycle,color):

    bicycle.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bicycle = Bicycle()

change_color(car1,"red")
change_color(car2,"blue")
change_color(car3,"white")
change_color(bicycle,"black")

print(car1.color)
print(car2.color)
print(car3.color)
print(bicycle.color)