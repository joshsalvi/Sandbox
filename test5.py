def xysum(x, y):
    if str(x).isdigit() and str(y).isdigit():
        return x + y
    else:
        return False

if __name__ == '__main__':
    assert xysum(1, 2) == 3, 'simple test'
    assert xysum(0, 0) == 0, 'zeros'
    assert xysum('a', 1) == False, 'Not a number'
