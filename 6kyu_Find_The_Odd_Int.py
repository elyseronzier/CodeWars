'''Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.'''



def find_it(seq):
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number
