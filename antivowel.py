def anti_vowel(text):
    result = text
    for letter in range(0,len(text)):
        if text[letter] in 'aeiouAEIOU':
            result = result.replace(result[letter], '.')
    result = result.replace('.','')
    return result

print anti_vowel('Canaries RUN VERY FAR!')