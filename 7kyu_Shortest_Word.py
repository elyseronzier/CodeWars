'''Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.'''



def find_short(s):
    len_list = []
    s = s.split(" ")
    for word in s:
        len_list.append(len(word))
    len_list.sort()
    return len_list[0]
