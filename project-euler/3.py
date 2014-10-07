import math
big_num = 600851475143

# find smallest factor
def smallest_factor(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return(i)

def is_prime(num):
    if num in range(2, 4):
        return(True)
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return(False)
        if i == int(math.sqrt(num)):
            return(True)
prime_factors = []

def find_factors(num):
    if is_prime(num):
        prime_factors.append(num)
    else: 
        find_factors(num / smallest_factor(num))

find_factors(big_num)

print prime_factors

#print is_prime(22)

#def prime_factors
