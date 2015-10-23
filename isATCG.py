def is_valid_sequence(seq):
    return len([x for x in seq if x.upper() != 'A' and x.upper() != 'G' and x.upper() != 'C' and x.upper() != 'T']) == 0


if __name__ == '__main__':
    assert is_valid_sequence('ATTTCCAAGGTGGG') == True
    assert is_valid_sequence('AaaaTcAccgGaTggG') == True
    assert is_valid_sequence('ATaaaCCggqTT') == False
