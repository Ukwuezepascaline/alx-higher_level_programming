#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = number % -10
else:
    lastd = number % 10
print('Last digit of {} is '.format(number), end="")
if lastd > 5:
    print('{} and is greater than 5'.format(lastd))
elif lastd == 0:
    print('{} and is 0'.format(lastd))
elif lastd < 6 and lastd != 0:
    print('{} and is less than 6 and not 0'.format(lastd))
Footer
