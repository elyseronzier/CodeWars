'''Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)] '''




def ordered_count(inp):
    lett_list = []
    numb_list = []
    result_list = []
    for char in inp:
        if char not in lett_list:
            lett_list.append(char)
            numb_list.append(inp.count(char))
            result_list.append((char,(inp.count(char))))
    return result_list  
