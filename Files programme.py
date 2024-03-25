# HOW TO WRITE FILES IN PYTHON
# text = "Yoooo What's good\nHow're you doing"
# with open('test.txt','w') as file:
#     file.write(text)

# HOW TO APPEND A FILE
# text = "\nYoooo What's good\nHow're you doing"
# with open('test.txt','a') as file:
#     file.write(text)


# HOW TO COPY A FILE
# import shutil
#
# shutil.copyfile('test.txt','copy.txt')


# HOW TO MOVE FILES USING PYTHON

import os

source = "copy.txt"
destination = "C:\\Users\\Ifeoluwa\\OneDrive\\Desktop\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source,"was moved")
except FileNotFoundError:
    print(source,"was not found")

