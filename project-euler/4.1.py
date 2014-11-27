product = 0
palindromes = []

for x in range(-999, -800):
    for y in range(-999, -800):
        product = x*y
        product_list = list(str(product))
        #checks if product is the same forwards and backwards
        if product_list == product_list[::-1]:
            palindromes.append(product)
            
def find_largest(number_list):
    biggest_number = 0
    for number in palindromes:
        if number > biggest_number:
            biggest_number = number

    print(biggest_number)

find_largest(palindromes)

