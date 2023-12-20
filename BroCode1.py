import time

name = ""

while len(name) == 0:
    name = input("What is your name? ")

print("Hello", name)

# while 1 == 1:
#     print("Help I'm stuck in the elevator")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy New Year!")