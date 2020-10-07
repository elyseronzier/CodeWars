'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

eg:
move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0] '''



def move_zeros(array):
    mid_list = []
    zero_list = []
    for numb in array:
        if numb != 0 or numb is False:
            mid_list.append(numb)
        else:
            zero_list.append(numb)
    return mid_list + zero_list
