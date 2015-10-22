def shift(listL, k):
    k = len(listL) - k
    right = listL[k::]
    left = listL[:k:]
    return right + left


def rotate(state, pipe_numbers):
    rotations = []
    for ind in range(0, len(state)):
        indices = 0
        shiftedstate = shift(state, ind)
        for num in pipe_numbers:
            if shiftedstate[num] == 1:
                indices += 1
        if indices == len(pipe_numbers):
            rotations.append(int(ind))
    return rotations


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
