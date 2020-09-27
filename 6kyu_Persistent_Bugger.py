'''Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.'''



import operator
import functools
def persistence(n, counter = 0):
    if (n < 10):
        return counter
    else:
        new_n = [int(digit) for digit in str(n)]
        solution_n = (functools.reduce(operator.mul,new_n))
        counter +=1
        if solution_n < 10:
            return counter
        else:
            return persistence(solution_n, counter)
