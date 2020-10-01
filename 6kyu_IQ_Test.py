'''Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd '''



def iq_test(numbers):
    new_list = [int(n) for n in numbers.split( )]
    odd_list = []
    even_list = []
    for numb in new_list:
        if numb % 2 == 0:
            even_list.append(numb)
        else:
            odd_list.append(numb)
    if len(even_list) == 1:
        for char in even_list:
            return new_list.index(char)+1
    if len(odd_list) == 1:
        for char in odd_list:
            return new_list.index(char)+1
