# Try to make a sum without using "sum, import, for, while, reduce"
def intadd(num, n, prevresult):
    if n >= 0:
        result = num[n] + prevresult
        result = intadd(num, n - 1, result)
        return result
    else:
        return prevresult


def creativesum(data):
    n = len(data) - 1
    return intadd(data, n, 0)


print creativesum([1, 2, 3, 4])
