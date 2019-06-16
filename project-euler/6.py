sum_square = 0
square_sum = 0

for x in range(1, 101):
    sum_square += x*x
    
for y in range(1, 101):
    square_sum += y

square_sum = (square_sum*square_sum)

print(square_sum - sum_square)

