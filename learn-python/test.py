import math

numbers = []
for i in range(1, 50):
    if i % 2 == 1:
        numbers.append(i)
print numbers


divisors = []
for i in numbers:
    specific_divisors = []
    for j in range(2, i):
        #if j == math.sqrt(i):
        #    divisors.append(specific_divisors)
        if i % j == 0:
            specific_divisors.append(j)
    divisors.append(specific_divisors)

print divisors
a = 1

primes = []
for i in divisors:
    if len(i) == 0:
       primes.append(a) 
    a += 2
    
print primes
    

