VOWELS = "aeiouy"


def translate(phrase):
    for index in range(0, len(phrase)):
        if phrase[index] not in VOWELS and phrase[index] != '-' and phrase[index] != ' ':
            phrase = phrase[:index + 1] + phrase[index + 1].replace(phrase[index + 1], '-') + phrase[index + 2:]
    phrase = phrase.replace('-', '')
    phrase = phrase.replace('aaa', 'a').replace('eee', 'e').replace('iii', 'i').replace('ooo', 'o').replace('uuu',
                                                                                                            'u').replace(
        'yyy', 'y')
    return phrase


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
