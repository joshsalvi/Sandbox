def censor(text, word1):
    return text.replace(word1, '*' * len(word1))

paragraph = 'In those five sentences, ' \
            'President Obama not only ticked off what' \
            ' he had done in his first term (equal pay for women, supporting gay' \
            ' marriage) but also what he wanted to do in his second term (climate ' \
            'change, gun control).  In those five sentences, too, Obama articulated' \
            ' the broader thematic of the speech: That we are all in this together' \
            ' and that we will ultimately judged by how we treat the lowest among ' \
            'us. In those five sentences Obama outlined what he wanted his second ' \
            'term to be -- and to mean.'
wordA = 'Obama'

import textwrap
print
print 'ORIGINAL PARAGRAPH:'
print textwrap.fill(paragraph,100)
print
print 'CENSORED PARAGRAPH:'
print textwrap.fill(censor(paragraph, wordA),100)
print
