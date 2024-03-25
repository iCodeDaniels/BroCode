class Airline:

    fly = True
    def length(self):
        print("All planes are at least 5 meters long")

    def engine(self):
        print("The engine of most planes are powered by a Rolls Royce engine")

class Etihad(Airline):
    def service(self):
        print("""This airline (Arguably) has the best first class suite and service(s)
And also cool amenity kits in nice color
    """)


etihad1 = Etihad()
etihad1.service()
etihad1.engine()
etihad1.length()






class Airline:
    def color(self):
        print("The color of planes generally is white. Except if customised")
    def length(self):
        print("The standard length of a commercial plane is 11 metres")
    def tyres(self):
        print("Air planes have 6 tyres all round")
    def engine(self):
        print("Most planes use the engine of a Rolls Royce")
class Singapore_Airways(Airline):
    def hospitality(self):
        print("The amenity kit in the singapore airline is really colorful and unique with amazing toys")
    def crew(self):
        print("The cabin crew consist of about 10-14 members")

class Fly_Emirates(Airline):
    def hospitality(self):
        print("Fly Emirates kits has to be the best")
    def crew(self):
        print("The cabin crew of the Fly Emirate are about 15 members")

Airline1 = Airline()
Airline1.color()
Airline1.length()
Airline1.engine()
Singapore_Airways1 = Singapore_Airways()
Singapore_Airways1.hospitality()
Singapore_Airways1.crew()
Fly_Emirates1 = Fly_Emirates()
Fly_Emirates1.hospitality()
Fly_Emirates1.crew()