# Challenge:

# Let's teach the Robots to distinguish words and numbers.
# You are given a string with words and numbers separated by whitespaces (one space).
# The words contains only letters. You should check if the string contains three words
# in succession. For example, the string "start 5 one two three 7 end" contains three
# words in succession.
# Input: A string with words.
# Output: The answer as a boolean.
# Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100

# My Solution:


def checkio(words):
    z = False
    y = 0
    x = words.split()
    for w in x:
        if w.isalpha():
            y += 1
            if y == 3:
                z = True
        else:
            y = 0
    return z