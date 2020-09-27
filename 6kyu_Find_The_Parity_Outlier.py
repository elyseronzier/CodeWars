'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N. '''




def find_outlier(integers):
    odd_list = []
    even_list = []
    for digit in integers:
        if digit % 2 == 0:
            even_list.append(digit)
        else:
            odd_list.append(digit)
    if len(odd_list) == 1:
        return odd_list[0]
    else:
        return even_list[0]
