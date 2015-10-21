def check_command(pattern, command):
    pattern = bin(pattern)
    pattern = pattern[2:]
    if len(command) > len(pattern):
        pattern = '0' * (len(command) - len(pattern)) + pattern
    elif len(pattern) > len(command):
        return False
    for ind in range(0, len(pattern)):
        if pattern[ind] == '1' and not command[ind].isalpha():
            return False
        elif pattern[ind] == '0' and command[ind].isalpha():
            return False
    else:
        return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, "12a0b3e4") == True, "42 is the answer"
    assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, "478103487120470129") == True, "Any number"
    assert check_command(127, "Checkio") == True, "Uppercase"
    assert check_command(7, "Hello") == False, "Only full match"
    assert check_command(8, "a") == False, "Too short command"
    assert check_command(5, "H2O") == True, "Water"
    assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"
