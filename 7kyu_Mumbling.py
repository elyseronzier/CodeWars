'''This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z. '''


def accum(s):
    solution_string = ""
    more_lett = 1
    counter = 1
    for lett in s:
        solution_string += lett * more_lett +"-"
        more_lett += 1
    solution_string = solution_string[0:len(solution_string)-1]
    return solution_string.title()
