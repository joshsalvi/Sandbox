def hammingdistance(n, m):
    x = bin(n ^ m)
    return x.count('1')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hammingdistance(117, 17) == 3, "First example"
    assert hammingdistance(1, 2) == 2, "Second example"
    assert hammingdistance(16, 15) == 5, "Third example"
