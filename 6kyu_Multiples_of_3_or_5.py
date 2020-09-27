'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.'''



def solution(number):
    sum_solution = 0
    for digit in range(number):
        if digit % 3 == 0 or digit % 5 == 0:
            sum_solution += digit
    return sum_solution
