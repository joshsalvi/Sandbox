def is_prime(x):    
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif isinstance(x, int) == False:
        return False
    else:
        counter = [0] * (x-2)
        for n in range(2,x):
            if x % n == 0:
                counter[n-2] = 0
            else:
                counter[n-2] = 1
        if 0 in counter:
            return False
        else:
            return True