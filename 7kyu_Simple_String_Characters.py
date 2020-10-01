'''In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.

More examples in the test cases.

Good luck! '''



def solve(s):
    turquoise = [0,0,0,0]
    for symbol in s:
        if symbol.isupper() == True:
            turquoise[0] += 1
        elif symbol.islower() == True:
            turquoise[1] += 1
        elif symbol.isnumeric() == True:
            turquoise[2] +=1
        else:
            turquoise[3] +=1
            
    return turquoise
