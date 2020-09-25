'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''


def pig_it(text):
    sep_words = text.split(" ")
    solution = []
    for char in sep_words:
        if char.isalpha():
            solution_words = char[1:]+char[0]+"ay"
            solution.append(solution_words)
        else:
            solution.append(char)
    return " ".join(solution)
    
    
