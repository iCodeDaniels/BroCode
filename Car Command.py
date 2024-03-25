command = ""
started = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("The car has started")
    elif command == "stop":
        print("The car is stopped")
        break
    elif command == "help":
        print('''
Start ---- Press the start button to put on the car
Stop ---- Press the stop button to put off the car
Quit ---- Quit brings the car to a total stop...
History ---- The car came into existence with the aim of pulling off the ground
        ''')
else:
    print("I can't process your input")
