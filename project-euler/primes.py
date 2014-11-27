import math
def test(n):
    if (n == 2) or (n == 3):
        return True
    if ((n % 2 == 0) or (n % 3 == 0)):
        return False
    for x in range(1, int(math.sqrt(n)) + 1):
        if ((n % (6*x + 1)) == 0) or ((n % (6*x - 1)) == 0):
            return False
        if (6*x + 1) >= (int(math.sqrt(n)) + 1):
            return True

