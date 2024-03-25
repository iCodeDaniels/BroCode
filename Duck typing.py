class Duck:

    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("The duck can talk")

class Chicken:

    def talk(self):
        print("The chicken clucks like a duck")

    def walk(self):
        print("The chicken can walk")

class Person():

    def catch(self,duck):
        duck.talk()
        duck.walk()
        print("We caught the duck")

duck = Duck()
chicken = Chicken()
person = Person()

(duck.walk())
(duck.talk())