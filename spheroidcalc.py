def checkio(height, width):
    import math
    a = float(width / 2)
    c = float(height / 2)
    if a < c:
        e = math.sqrt(1 - (a ** 2) / (c ** 2))
        volume = 4 * math.pi / 3 * (a ** 2) * c
        area = 2 * math.pi * (a ** 2) * (1 + c / a / e * math.asin(e))
    elif c < a:
        e = math.sqrt(1.0 - (c ** 2) / (a ** 2))
        volume = 4.0 * math.pi / 3 * (a ** 2) * c
        area = 2.0 * math.pi * (a ** 2) * (1 + (1 - (e ** 2)) / e * math.atanh(e))
    else:
        volume = 4.0 / 3.0 * math.pi * (a ** 3)
        area = 4.0 * math.pi * (a ** 2)

    return [float("{0:.2f}".format(volume)), float("{0:.2f}".format(area))]


print checkio(2, 2)
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
