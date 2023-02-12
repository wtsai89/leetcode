from cs50 import *

number = get_int("Number: ")

copy = number
length = 0
sum = 0
while copy:
    sum += copy % 10
    copy = copy // 10
    length += 1
    if not copy:
        break
    double = (copy % 10) * 2
    while double:
        sum += double % 10
        double = double // 10
    copy = copy // 10
    length += 1

if sum % 10:
    print("INVALID")
elif length == 15:
    firstTwo = number // pow(10,13)
    print(firstTwo)
    if firstTwo == 34 or firstTwo == 37:
        print("AMEX")
    else:
        print("INVALID")
elif length == 16:
    firstTwo = number // pow(10,14)
    if 51 <= firstTwo <= 55:
        print("MASTERCARD")
    elif firstTwo // 10 == 4:
        print("VISA")
    else:
        print("INVALID")
elif length == 13:
    firstTwo = number // pow(10,11)
    if firstTwo // 10 == 4:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")