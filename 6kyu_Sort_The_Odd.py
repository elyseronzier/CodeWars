'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

'''


def sort_array(array):
    result = []
    sort_odds =sorted([x for x in array if x%2])
    counter = 0
    for num in array:
        if num % 2:
            result.append(sort_odds[counter])
            counter += 1
        else:
            result.append(num)
    return result
