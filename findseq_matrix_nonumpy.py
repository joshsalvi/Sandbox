def checkio(mat):
    diag = []
    for ind1 in range((-len(mat)), (len(mat))):
        for ind2 in (-1, 1):
            diag.append([row[ind2 * i + ind1] for i, row in enumerate(mat) if 0 <= ind2 * i + ind1 < len(row)])
    mtrans = [[row[i] for row in mat] for i in range(len(mat[0]))]
    counter = 0
    for ind1 in range(0, len(mat)):
        val = 0
        for ind2 in range(0, len(mat)):
            if ind2 == 0:
                val = mat[ind1][ind2]
                counter = 1
            elif mat[ind1][ind2] == val:
                counter += 1
            else:
                val = mat[ind1][ind2]
                counter = 1
            if counter >= 4:
                return True
    for ind1 in range(0, len(mat)):
        val = 0
        for ind2 in range(0, len(mat)):
            if ind2 == 0:
                val = mtrans[ind1][ind2]
                counter = 1
            elif mtrans[ind1][ind2] == val:
                counter += 1
            else:
                val = mtrans[ind1][ind2]
                counter = 1
            if counter >= 4:
                return True
    for ind1 in range(0, len(diag)):
        val = 0
        if len(diag[ind1]) >= 4:
            for ind2 in range(0, len(diag[ind1])):
                if ind1 == 0:
                    val = diag[ind1][ind2]
                    counter = 1
                elif diag[ind1][ind2] == val:
                    counter += 1
                else:
                    val = diag[ind1][ind2]
                    counter = 1
                if counter >= 4:
                    return True
    if counter < 4:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
