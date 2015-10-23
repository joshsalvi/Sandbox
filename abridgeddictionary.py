abridged_english_dictionary = dict(cat="a lion, tiger, leopard, or similar wild animal",
                                   dog="a domestic mammal closely related to the gray wolf",
                                   wizard="a person who is skilled in magic")


def word_with_longest_definition(d):
    items = d.items()
    longest_definition_compare = ''
    longest_definition = ''
    for item in items:
        if len(item[1]) > len(longest_definition_compare):
            longest_definition_compare = item[1]
            longest_definition = item[0]
    return longest_definition


print word_with_longest_definition(abridged_english_dictionary)

if __name__ == '__main__':
    assert word_with_longest_definition(abridged_english_dictionary) == 'dog'
