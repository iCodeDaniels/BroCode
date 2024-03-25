# HOW TO REMOVE A FILE

import os

try:
    os.remove('testfile.txt')
except FileNotFoundError:
    print("That file was not found")