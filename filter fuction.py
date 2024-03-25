party_names = [("Johnson",19),
               ("Winifred",22),
               ("Phoebe",18),
               ("Ifeoluwa",20),
               ("Max",17),
               ("Rhoda",17)]

age = lambda ages:ages[1] >= 18

drinking_buddies = list(filter(age, party_names))

for i in drinking_buddies:
    print(i)