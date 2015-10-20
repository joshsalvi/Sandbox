def anti_vowel(text):
    result = text
    for letter in range(0, len(text)):
        if text[letter] in 'aeiouAEIOU':
            result = result.replace(result[letter], '.')
    result = result.replace('.', '')
    assert isinstance(result, str)
    return result


if __name__ == '__main__':
    assert anti_vowel('Canaries RUN VERY FAR!') == 'Cnrs RN VRY FR!'
    assert anti_vowel(
        'Pablo Escobar was a very bad man, but it was a beautiful story!') == 'Pbl scbr ws  vry bd mn, bt t ws  btfl ' \
                                                                              'stry!'
    assert anti_vowel('I\'m Ron Burgundy?') == '\'m Rn Brgndy?'
