from cs50 import *

height = -1
while height < 1 or height > 8:
    height = get_int("Height: ")

for i in range(1,height+1):
    print(" " * (height-i) + "#" * i + "  " + "#" * i)