millionaire = ["Daniel","Timilehin","Ifeoluwa","Faith"]

sorted_millionaire = sorted(millionaire)

for i in sorted_millionaire:
    print(i)



student = [("Squidward","F",60),
           ("Sandy","A",33),
           ("Patrick","D",36),
           ("Spongebob","B",20),
           ("Krabs","C",78)]

name = lambda name:name[0]
student.sort(key=name)

for i in student:
    print(i)