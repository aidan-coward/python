import math

def is_prime(number):
    upper_bound = int(math.sqrt(number))
    if ((number == 2) or (number == 3)):
        return True

    for x in range(2, (upper_bound + 1)):
        if (number % x == 0):
            return False

        if x == upper_bound:
            return True


counter = 1 
number = 0 

while counter <= 10001:
    if is_prime(number):
        print(number)
        counter += 1
        if counter == 10001:
            print(number)

    number += 1

