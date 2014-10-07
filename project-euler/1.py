# try with pop next

threes = [3]
fives = [5]

counter = 6
total_counter = 8

while counter < 999:
    print counter, total_counter
    if (counter % 3 == 0) or (counter % 5 ==0):
        total_counter += counter
        counter += 1
    else:
        counter += 1
    print counter, total_counter
    print "-----"

print total_counter + 999
