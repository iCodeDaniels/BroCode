import random

# FOR PICKING 5 RANDOM NUMBERS FROM: 10 - 20
for i in range(5):
    print(random.randint(10, 20))


# FOR PICKING AN ITEM OR OBJECT FROM THE LIST
members = ['John', 'Mary', 'Bob', 'James']
leader = random.choice(members)
print(leader)