numbers = []

def while_loop(x, y):
    for j in range(0, x + 1):
        print "At the top i is %d" % j
        numbers.append(j)
        j = j + y 
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % j

print while_loop(20, 4)
