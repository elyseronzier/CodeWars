'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate. Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!'''


def duplicate_encode(word):
    low_word = word.lower()
    solution = []
    for char in low_word:
        if low_word.count(char) == 1:
            solution.append("(")
        else:
            solution.append(")")

    return ''.join(solution)
