#divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def is_modulo(number):
    results = []
    for divisor in divisors:
        if number % divisor == 0:
            results.append(True)

    if len(results) == 20:
        return True
    else: 
        return False

big_number = 2520
while is_modulo(big_number) == False:
#    print(big_number, "No")
    big_number += 10

print("Yes: %r" % big_number)


