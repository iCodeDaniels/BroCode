class Animal:

    alive = True

    def eat(self):
        print("This rabbit is eating")

class Rabbit(Animal):

    def eat(self):
        print("Rabbits in general eats carrot")

Rabbit = Rabbit()
Rabbit.eat()