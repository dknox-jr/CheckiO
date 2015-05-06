# Challenge:

# For language training our Robots want to learn about suffixes.
# In this task, you are given a set of words in lower case.
# Check whether there is a pair of words, such that one word
# is the end of another (a suffix of another).
# For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.
# Input: Words as a set of strings.
# Output: True or False, as a boolean.
# Precondition: 2 ≤ len(words) < 30
# all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

# My Solution:


def checkio(words_set):
    for w in words_set:
        for x in words_set:
            if w != x and x.endswith(w):
                return True        
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"