def checkio(mat):
    import numpy as np
    m = np.matrix(mat)
    diags = [m[::-1, :].diagonal(i) for i in range(-m.shape[0] + 1, m.shape[1])]
    diags.extend(m.diagonal(i) for i in range(m.shape[1] - 1, -m.shape[0], -1))
    diags = [n.tolist() for n in diags]
    mtrans = m.transpose()
    counter = 0
    for ind1 in range(0, len(m)):
        val = 0
        for ind2 in range(0, len(m)):
            if ind2 == 0:
                val = m.item(ind1, ind2)
                counter = 1
            elif m.item(ind1, ind2) == val:
                counter += 1
            else:
                val = m.item(ind1, ind2)
                counter = 1
            if counter >= 4:
                return True
    for ind1 in range(0, len(m)):
        val = 0
        for ind2 in range(0, len(m)):
            if ind2 == 0:
                val = mtrans.item(ind1, ind2)
                counter = 1
            elif mtrans.item(ind1, ind2) == val:
                counter += 1
            else:
                val = mtrans.item(ind1, ind2)
                counter = 1
            if counter >= 4:
                return True
    for ind1 in range(0, len(diags)):
        val = 0
        if len(diags[ind1][0]) >= 4:
            for ind2 in range(0, len(diags[ind1][0])):
                if ind1 == 0:
                    val = diags[ind1][0][ind2]
                    counter = 1
                elif diags[ind1][0][ind2] == val:
                    counter += 1
                else:
                    val = diags[ind1][0][ind2]
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
