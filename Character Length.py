#A CERTAIN AMOUNT OF CHARACTERS
name = input("What is your full name?: ")

if len(name) < 3:
     print("The name must be at least 3 characters long")
elif len(name) > 50:
     print("The name must be a maximum of 50 characters")
else:
    print("A valid name")