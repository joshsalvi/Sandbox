VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.upper()
    text = text.split(' ')
    counter = 0
    for ind in range(0, len(text)):
        for indL in range(0, len(text[ind])):
            if indL == 0 and text[ind][indL] in VOWELS:
                letter = 'V'
            elif indL == 0 and text[ind][indL] in CONSONANTS:
                letter = 'C'
            elif letter == 'C' and text[ind][indL] in VOWELS:
                letter = 'V'
            elif letter == 'V' and text[ind][indL] in CONSONANTS:
                letter = 'C'
            else:
                letter = 'X'
        if len(text[ind]) < 2:
            letter = 'X'
        if letter == 'C' or letter == 'V':
            counter += 1
    return counter


print checkio("A quantity of striped words.")

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
