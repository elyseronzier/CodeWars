'''
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
'''



def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    result = []
    bin_it = []
    for i in arr:
        if result and dict.get(i) == result[-1]:
            result.pop(-1)
            bin_it.append(-1)
        else:
            result.append(i)
    return result
    
    
    
