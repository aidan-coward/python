import math

def smallest_factor(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return(i)


# num -> [num]
# takes a number and produces a list with the inputted number as the final entry 
# and its factors as preceding entries
def find_factors(num):
    num_and_factors = []
    for i in reversed(range(100, 1000)):
        if num % i == 0:
            num_and_factors.append(i)
        if i == 100:
            num_and_factors.append(num)
            return num_and_factors

# [num] -> [num]
def largest_factors(arg):
    num = arg.pop()
    for i in arg:
        for j in arg:
            if i * j == num:

                





print find_factors(8888888888)


