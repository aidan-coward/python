import math
#find all pythagorean triplets where a,b,c <= 998
perfect_squares = []
number = 1
while len(perfect_squares) <= 500:
    perfect_squares.append(number*number)
    number += 1

triples_list = []
for a in range(1, 999):
    for b in range(a, 999):
        if ((a*a + b*b) in perfect_squares) and (int(math.sqrt(a*a + b*b)) + a + b == 1000):
            print(a*b*int(math.sqrt(a*a + b*b)))
