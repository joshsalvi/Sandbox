def flat_list(array):
    i = array
    if isinstance(i, list):
        return [a for i in i for a in flat_list(i)]
    else:
        return [i]


# Check the code
if __name__ == '__main__':
    assert flat_list([1, 2, 3]), 'Simple list'
    assert flat_list([1, [1, 2, 3], 3]), 'One nested list'
    assert flat_list([1, [1, 2, [1, 2], [1, 2, [1, 2, 5]]], 3]), 'Multiple nested lists'
    assert flat_list([0]), 'Single element'
