BRACKET_PAIRS = ['()', '{}', '[]', '<>']
OPEN_BRACKETS = {a for a, _ in BRACKET_PAIRS}
CLOSE_BRACKETS = {b: a for a, b in BRACKET_PAIRS}


def checkio(data):
    stack = []
    for ch in data:
        if ch in OPEN_BRACKETS:
            stack.append(ch)
        elif ch in CLOSE_BRACKETS:
            if not stack or stack[-1] != CLOSE_BRACKETS[ch]:
                return False
            stack.pop()
    return not stack


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
