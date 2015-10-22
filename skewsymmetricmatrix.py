def checkio(matrix):
    for ind1 in range(0, len(matrix)):
        for ind2 in range(0, len(matrix[0])):
            if matrix[ind1][ind2] != -1 * matrix[ind2][ind1]:
                return False
    else:
        return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
