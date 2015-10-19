def checkio(text, word):
    text = text.replace(' ', '').lower().split('\n')
    horz = [[row + 1, line.find(word) + 1, row + 1, line.find(word) + len(word), line] for row, line in enumerate(text)
            if line.find(word) >= 0]
    words_transp = [''.join(t) for t in zip(*text)]
    vert = [[line.find(word) + 1, col + 1, line.find(word) + len(word), col + 1, line] for col, line in
            enumerate(words_transp) if line.find(word) >= 0]
    if horz:
        return horz[0][0:4]
    elif vert:
        return vert[0][0:4]
    else:
        return []


print checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten")

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
