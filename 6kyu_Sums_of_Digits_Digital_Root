'''Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.'''



def digital_root(n):
    if (n < 10):
        return n
    else:
        new_n = [int(i) for i in str(n)]
        solution_n = sum(new_n)
        if solution_n < 10:
            return solution_n
        else:
            return digital_root(solution_n)
