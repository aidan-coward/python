import math

def is_prime(number):
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True 

prime_list = []

for x in range(2, 2000000):
    if is_prime(x):
        prime_list.append(x)

prime_sum = 0

for x in prime_list:
    prime_sum += x

print(prime_sum)
