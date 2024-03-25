class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey,Predator):
    pass

Rabbit = Rabbit()
Rabbit.flee()

Lion = Lion()
Lion.hunt()

Fish = Fish()
Fish.flee()
Fish.hunt()