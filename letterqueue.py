def letter_queue(commands):
    result = ''
    for cmd in commands:
        if cmd[0:4] == 'PUSH':
            result += cmd[5]
        elif cmd[0:3] == 'POP':
            if len(result) > 0:
                result = result[1:]
            else:
                result = ''
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
