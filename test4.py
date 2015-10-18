def checkio(a, b, c):
    import math
    angles = [0, 0, 0]
    if (c ** 2 - b ** 2 - a ** 2) / (-2.0 * a * b) >= -1 and (a ** 2 - c ** 2 - b ** 2) / (-2.0 * b * c) >= -1 and (
                b ** 2 - a ** 2 - c ** 2) / (-2.0 * c * a) >= -1:
        angles[0] = round(math.degrees(math.acos((c ** 2 - b ** 2 - a ** 2) / (-2.0 * a * b))))
        angles[1] = round(math.degrees(math.acos((a ** 2 - c ** 2 - b ** 2) / (-2.0 * b * c))))
        angles[2] = round(math.degrees(math.acos((b ** 2 - a ** 2 - c ** 2) / (-2.0 * c * a))))
    if 0 in angles:
        angles = [0, 0, 0]
    return sorted(angles)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    # assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(10, 20, 30) == [0, 0, 0]
