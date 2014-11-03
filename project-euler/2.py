a = 1
c = 1 
b = 2
terms = []
counter = 1

while a < 4000000:
    if a % 2 == 0:
        terms.append(a)
    c = a
    a = b
    b = b + c
    print terms
    counter += 1

print sum(terms) 
