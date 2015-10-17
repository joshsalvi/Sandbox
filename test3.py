import math as mth


def formula_calc():
    items = [x for x in raw_input().split(',')]
    Q = []
    C = 50
    H = 30
    for value in items:
        Q.append(str(int(round(mth.sqrt((2 * C * float(value)) / H)))))
    return Q


print formula_calc()


def yrange(x):
    ind = 0
    while ind < x:
        yield ind
        ind += 1
    else:
        yield ind


y = yrange(10)

print y.next()
print y.next()
print y.next()
